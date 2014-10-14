# template for "Stopwatch: The Game"
import simplegui
# define global variables
canvas_width = 500
canvas_height = 400
# time_reset = 0
time_start = 0
time_pause = 0
success_time = 0
total_time = 0
timer_stop = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	
	result_min = int(t/600)
	result_second = int(t/10) % 60
	if result_min < 10:
		result_min_str = "0" + str(result_min)
	else:
		result_min_str = str(result_min)
	if result_second < 10:
		result_second_str = "0" + str(result_second)
	else:
		result_second_str = str(result_second)

	result_mimisec = t %10

    return result_min_str+":" + result_second_str + ":" + str(result_mimisec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
	global time_start
	time_start = time_pause
	timer.start()
	timer_stop = False
def stop_button():
	global time_pause
	global success_time
	global total_time
	timer.stop()
	time_pause = time_start
	timer_stop = True
	if timer_stop:
		if time_start % 10 == 0:
			success_time += 1
			total_time += 1
		else:
			total_time += 1

def reset_button():
	global time_start
	global time_pause
	global success_time
	global total_time
	timer.stop()
	time_start = 0
	time_pause = 0
	success_time = 0
	total_time = 0
# define event handler for timer with 0.1 sec interval
def timehandler():
	global time_start
	if time_start <36000:
		time_start += 1
	else:
		time_start = 0


# define draw handler

def draw(canvas):
	count = str(success_time)+"/"+str(total_time)
	canvas.draw_text(format(time_start),[60,110],24,"White")
	canvas.draw_text(count,[400,40],10,"White")
# create frame

frame = simplegui.create_frame("StopWatch", canvas_width, canvas_height)
# register event handlers
frame.set_draw_handler(draw)
frame.add_button("start", start_button, 100)
frame.add_button("stop", stop_button, 100)
frame.add_button("reset", reset_button,100)
timer = simplegui.create_timer(100,timehandler)

# start frame
frame.start()
# timer.start()
# Please remember to review the grading rubric