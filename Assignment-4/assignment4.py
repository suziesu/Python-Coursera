# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [HALF_PAD_WIDTH,HEIGHT/2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
VEL = 4
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel= 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
    # ball_vel = [random.randrange(120,240),random.randrange(60,180)]

    if not direction:
        ball_vel[0] = - random.randrange(2,4)
        ball_vel[1] = - random.randrange(1,3)
        # ball_pos = [WIDTH/2 - ball_vel[0],HEIGHT/2 - ball_vel[1]]
    else:
        ball_vel[0] = random.randrange(2,4)
        ball_vel[1] = - random.randrange(1,3)
        # ball_pos = [WIDTH/2 + ball_vel[0],HEIGHT/2 - ball_vel[1]]
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]

    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos = [WIDTH/2,HEIGHT/2]
    paddle1_pos = [paddle1_pos[0], paddle1_pos[1] + paddle1_vel]
    paddle2_pos = [paddle2_pos[0], paddle2_pos[1] + paddle2_vel]

    direction_choice = [LEFT,RIGHT]
    # direction = [random.randrange(120,240), random.randrange(60,180)]
    spawn_ball(random.choice(direction_choice))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]

    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT :
            ball_pos = [WIDTH/2,HEIGHT/2]
            score2 += 1
            ball_vel[0] = - random.randrange(2,4)
            ball_vel[1] = - random.randrange(1,3)
        else:
            ball_vel[0] = - ball_vel[0]
            ball_vel = [x * 1.1 for x in ball_vel]
    elif ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] < paddle2_pos[1] - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos[1] + HALF_PAD_HEIGHT :
            ball_pos = [WIDTH/2,HEIGHT/2]
            score1 += 1
            ball_vel[0] = - random.randrange(2,4)
            ball_vel[1] = - random.randrange(1,3)
        else:
            ball_vel[0] = - ball_vel[0] 
            ball_vel = [x * 1.1 for x in ball_vel]
    elif ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        ball_vel[0] = - ball_vel[0]
    else:
        ball_vel[1] = ball_vel[1]           
        ball_vel[0] = ball_vel[0]
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]           

    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,5,"White","White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = [paddle1_pos[0], paddle1_pos[1] + paddle1_vel]
    paddle2_pos = [paddle2_pos[0], paddle2_pos[1] + paddle2_vel]

    if (paddle1_pos[1] + paddle1_vel) >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = [paddle1_pos[0], HEIGHT - HALF_PAD_HEIGHT]
    elif (paddle1_pos[1] + paddle1_vel) <= HALF_PAD_HEIGHT:
        paddle1_pos = [paddle1_pos[0], HALF_PAD_HEIGHT]
    else:
        paddle1_pos= [paddle1_pos[0],paddle1_pos[1]+paddle1_vel] 
    if (paddle2_pos[1] + paddle2_vel) >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = [paddle2_pos[0], HEIGHT - HALF_PAD_HEIGHT]
    elif (paddle2_pos[1] + paddle2_vel) <= HALF_PAD_HEIGHT:
        paddle2_pos = [paddle2_pos[0], HALF_PAD_HEIGHT]
    else:
        paddle2_pos= [paddle2_pos[0],paddle2_pos[1]+paddle2_vel] 
    
    # draw paddles
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0],paddle1_pos[1] + HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0],paddle2_pos[1] + HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 100,100],10,"White")
    canvas.draw_text(str(score2), [WIDTH/2 + 100,100],10,"White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = - VEL
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = VEL
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -VEL
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("restart", new_game,100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
