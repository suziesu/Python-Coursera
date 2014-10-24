# implementation of card game - Memory

import simplegui
import random
#list of range [0,8) = list = range(8)
# cannot use list[0],[1] without initiate, use append instead
#clear all item list[:] = []

listAll = []
exposed = []
flipturn = 0
state = 0
previouscardnumber = []
previouscard = []
# helper function to initialize globals
def new_game():
	global listAll,exposed,state,flipturn,previouscardnumber,previouscard
	exposed = []
	previouscardnumber[:] = []
    previouscard[:] = []
	state = 0
	flipturn = 0
    listAll = setnumber()
    for i in range(16):
    	exposed.append(False)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,flipturn,state,listAll,previouscardnumber,previouscard
    cardNumber = -1

    if pos[0] > 800 or pos[0] < 0 or pos[1] > 100 or pos[1] < 0:
    	print "out of range"
    else:
    	cardNumber = cardnumber(pos[0]) 
    if cardNumber > -1 and exposed[cardNumber] == False:
    	exposed[cardNumber] = True
    	flipturn += 1
    	if state == 0:
    		state = 1
    		previouscard.append(listAll[cardNumber])
    		previouscardnumber.append(cardNumber)
    	elif state == 1:
    		previouscard.append(listAll[cardNumber])
    		previouscardnumber.append(cardNumber) 
    		state = 2
    	else:
    		if previouscard[0] != previouscard[1]:
    			for k in previouscardnumber:
    				exposed[k] = False
    			print exposed
    		previouscardnumber[:] = []
    		previouscard[:] = []
    		previouscard.append(listAll[cardNumber])
    		previouscardnumber.append(cardNumber)
    			# exposed[x for x in previouscardnumber] = False
    		state = 1 
    



def cardnumber(po):
	return int(po/50)    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
	global listAll,exposed,flipturn

	i = [25,50]
	j = 0
	# cardpos = [[0,0],[0,100],[50,100],[50,0]]
	for number in listAll:
		canvas.draw_text(str(number),i,12,"Yellow")
		i[0] += 50
		if exposed[j] == False:
			canvas.draw_polygon(card(j),10,"Black","Green")
		j += 1
	label.set_text(flipturn)
		
def card(j):
	return [[50*j, 0],[50*j, 100], [50*(j+1), 100],[50*(j+1),0]]

def setnumber():
	listA = range(8)
	listB = range(8)
	listA.extend(listB)
	random.shuffle(listA)
	return listA

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric