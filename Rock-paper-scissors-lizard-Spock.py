import math
import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):

    if name == "rock":
    	number = 0
    elif name == "Spock":
    	number = 1
    elif name == "paper":
    	number = 2
    elif name == "lizard":
    	number = 3
    elif name == "scissors":
    	number = 4
    else:
    	print "Not A Valid item!"
    	number = -1
    return number

def number_to_name(number):
    
    if number == 0:
    	name = "rock"
    elif number == 1:
    	name = "Spock"
    elif number == 2:
    	name = "paper"
    elif number == 3:
    	name = "lizard"
    elif number == 4:
    	name = "scissors"
    else:
    	print "Number is not Valid"
    	name = False
    return name

def rpsls(player1, player2): 
    result = (player1-player2) % 5
    if result == 0 :
    	return 0
    elif result >= 3:
    	return -1
    	# player 2 win
    elif result <3 and result >0:
    	return 1
    	#player 1 win
    
if __name__ == "__main__":
	while True:
		print "\n"
		player_choose = raw_input("Player choose :")
		player_number = name_to_number(player_choose)
		computer_number = random.randrange(0,5)
		computer_choose = number_to_name(computer_number)
		print "Computer Choose: %s" %(computer_choose)
		if player_number >= 0 and computer_choose:
			out = rpsls(player_number, computer_number) 
			if out == 0:
				print "it is a tie"
			elif out == 1:
				print "Player Win"
			elif out == -1:
				print "Computer Win"
			else:
				print "Wrong output"
		else:
			print "Input is Wrong or Computer is Wrong!"
			
