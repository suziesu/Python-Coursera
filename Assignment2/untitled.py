import simplegui 
import random
"""
Set globals
Helper function
Classes
Define event handlers
Create a frame
Register event handlers 
Start frame & timers

"""
# Define global var
secret_number = 0
remain_number = 0
choice_number = 0
def new_game(choice):
    global secret_number
    global choice_number
    secret_number = 0
    choice_number = choice
    print "new game range is from 0 to %d" %(choice)
    secret_number = random.randrange(0,choice)



# Define helper function

# Define event handlers
def range100():
    global remain_number
    remain_number = 7
    new_game(100)

def range1000():
    global remain_number
    remain_number = 10
    new_game(1000)

def input_guess(guess):
    getInput = int(guess)
    print "Guess was %d" %(getInput)
    global remain_number
    remain_number = remain_number - 1
    print "Number of remaining guess is %d" %(remain_number - 1)
    if choice_number == 0 or remain_number == 0:
        print "no choice set or no remain try"
        return
    elif getInput > choice_number:
        print "exceed the max number"
    elif getInput > secret_number:
        print "lower"
    elif getInput < secret_number:
        print "higher"
    else:
        print "congrats"



# Create a frame
frame = simplegui.create_frame("guess a number", 200, 200)

# Register event handlers
frame.add_button("range100",range100,100)
frame.add_button("range1000", range1000,100)
frame.add_input("Guess a number",input_guess,100)
# Start frame and timers
frame.start()
