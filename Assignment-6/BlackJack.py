# Mini-project #6 - Blackjack

import simplegui
import random
import time

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

DEALER_CARD_P = [50,150]
PLAYER_CARD_P =[50,450]

# initialize global variables
deck = []
in_play = False
outcome = ""
score = 0
DEALER_TEXT = "Dealer"
PLAYER_TEXT = "Player"
DEALER_MESSAGE = ""

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", self.suit, self.rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, pos, CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        	# replace with your code
        self.handList = []
    def __str__(self):
    	# replace with your code
        return self.handList

    def add_card(self, card):
    	# replace with your code
        self.handList.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if don't bust
    def get_value(self):
        # replace with your code
        handValue = 0
        for card in self.handList:
            handValue += VALUES[card.get_rank()]
        for card in self.handList:
            if 'A' == card.get_rank() and handValue + 10 <= 21:
                handValue += 10
        return handValue


    def busted(self):
        # replace with your code
        return self.get_value() > 21

    
    def draw(self, canvas, p):
        # replace with your code
        if self.handList:
            i = 0
            for card in self.handList:
                # print card.get_rank()
                if p[1] == DEALER_CARD_P[1] and in_play and i == 1:
                    canvas.draw_image(card_back,[CARD_BACK_SIZE[0]/2,CARD_BACK_SIZE[1]/2],CARD_BACK_SIZE,[p[0] + CARD_SIZE[0],p[1]],CARD_SIZE)
                    i += 1
                    # p[0] += CARD_SIZE[0] 
                else:
                   card.draw(canvas, [p[0] + i*CARD_SIZE[0],p[1]])
                   i += 1
                    # p[0] += CARD_SIZE[0] 

 
player = Hand()
dealer = Hand()        
# define deck class
class Deck:
    def __init__(self):
        self.selfDeck = []
        countN = 0
        # replace with your code
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit,rank)
                self.selfDeck.append(card)

    # add cards back to deck and shuffle
    def shuffle(self):
        	# replace with your code
        random.shuffle(self.selfDeck)

    def deal_card(self):
        	# replace with your code
        return self.selfDeck.pop()


#define callbacks for buttons
def deal():
    global outcome, in_play, player, dealer,deck,player,dealer
    outcome = ""
    in_play = False
    deck = []
    player = Hand()
    dealer =Hand()
    deckObj = Deck()
    deckObj.shuffle()

    # for i in range(2):
    player.add_card(deckObj.deal_card())
    dealer.add_card(deckObj.deal_card())
    player.add_card(deckObj.deal_card())
    dealer.add_card(deckObj.deal_card())
    deck = deckObj.selfDeck
    # print len(player.handList)
    # your code goes here
    
    outcome = "Hit or Stand ?"
    in_play = True

def hit():
    global in_play,score,outcome,DEALER_MESSAGE
    print player.busted()
    # if the hand is in play, hit the player
    if in_play and player.busted()==False:
        player.add_card(deck.pop())
        if player.busted():
            outcome = "Busted, You Lose"
            DEALER_MESSAGE = "New Deal?"
            in_play = False
            score -= 1
        elif player.get_value() == 21:
            outcome = "Congrats, You win"
            DEALER_MESSAGE = "New Deal?"
            in_play = False
            score += 1
    else:
        pass
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global in_play,score,outcome,DEALER_MESSAGE
    # replace with your code below
    if in_play:
        in_play = False
        while dealer.get_value() < 17 :
            dealer.add_card(deck.pop())
        if dealer.busted or dealer.get_value() < player.get_value():
            DEALER_MESSAGE = "Dealer Lose"
            outcome = "You win"
            score += 1
        else:
            DEALER_MESSAGE = "Dealer Win"
            score -= 1
            outcome = "You Lose! New Deal?"
    else:
        return
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def draw(canvas):
    # replace with your code below
    canvas.draw_text("BLACKJACK",[30,30],30,"White")
    canvas.draw_text(outcome, [300,300],20,"White")
    canvas.draw_text(DEALER_TEXT,[50,80],20, "White")
    canvas.draw_text(PLAYER_TEXT,[50,300],20, "White")
    canvas.draw_text(DEALER_MESSAGE,[300,80],20, "White")
    canvas.draw_text(str(score),[300,30],30,"White")
    player.draw(canvas,PLAYER_CARD_P)
    dealer.draw(canvas,DEALER_CARD_P)    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()


