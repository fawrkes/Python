/* 
*   Bouncy the amazing bouncy ball!
*  This program is a GUI for initializing a window,
*  creating bouncy and telling him where you want him
*  to bounce.
*/

from Tkinter import *
import Tkinter,time
global Start_button

def exit_bouncy():
    Game.destroy()
    Instructions.destroy()
    
def start_bouncing():
    global ball, slope, square, meridinal_velocity, zonal_velocity, N, S, E, W, hit
    

    # instructions stuff
    square.unbind("<Button-1>")
    Quit = Tkinter.Button(text = "Quit", command = exit_bouncy)
    Quit.grid(row = 4,column = 0)

    ######## MAJOR LOOP ##########
    bypass = 1
    while True:

        # compass directions
        NW = (x_slope < x_start and y_slope < y_start)
        SE = (x_slope > x_start and y_slope > y_start)
        NE = (x_slope > x_start and y_slope < y_start)
        SW = (x_slope < x_start and y_slope > y_start)

        # gets bouncy started from the original mouse inputs
        if bypass == 1:
            
            # configure rise/run
            
            if SE or NE or NW or SW:
                   
                   if SW or NW:
                      
                       meridinal_velocity = slope
                      
                       #set to '3' in the interest of speed
                       zonal_velocity = -3
                       bypass = 2
                   
                   elif NE or SE:
                       meridinal_velocity = -1*slope
                       
                       #set to '3' in the interest of speed
                       zonal_velocity = 3 
                       bypass = 2

        square.move(ball, zonal_velocity, meridinal_velocity)

        #check for when to bounce
        N = square.coords(ball)[1] < 5
        S = square.coords(ball)[3] > 498
        E = square.coords(ball)[2] > 498
        W = square.coords(ball)[0] < 4

        # bounce
        if N or S or E or W:

            if N or S:
                meridinal_velocity = meridinal_velocity * -1
                # print "Boing..."

            elif E or W:
                zonal_velocity = zonal_velocity * -1
                #print "Boing..."
            
        square.update()
        

def slope_sign():
    global slope_num, slope_den, x_start, y_start, x_slope, y_slope, slope, Start_button
    
    # check/operation on sign of slope
    if (x_slope < x_start and y_slope < y_start) or (x_slope > x_start and y_slope > y_start):
        #set to '3' in the interest of speed
        slope = -3*slope 

    start_bouncing()
    

def configure_slope():
    global slope_num, slope_den, x_start, y_start, x_slope, y_slope, slope, Start_button
    
    slope = slope_num/slope_den

    #rounding the slope to hundreth digits

    slope1 = str(slope_num/slope_den)

    if len(slope1) > 3:
        slope1 = float(slope1[:4])
        slope = slope1

    slope_sign()


def get_slope(event):
    global x_start, y_start, slope_num, slope_den, x_slope, y_slope, Start_button
    
    # for programmers use
    print "Slope determinant coordinates:", event.x, event.y

    # retrieve the slope indicator coordinates
    x_slope = int(event.x)
    y_slope = int(event.y)

    # next instructions
    Start_Label = Tkinter.Label(text="Please press the start button when "\
                                "you would like bouncy to start bouncing.")
    Start_Label.grid(row=3,column=0)

    Start_Button = Tkinter.Button(text="Start",command=configure_slope)
    Start_Button.grid(row=4,column=0)

    # create variables for slope configuration
    slope_num = float(abs(y_start-y_slope))
    slope_den = float(abs(x_start-x_slope))

def make_start_ball():
    global x_start,y_start,ball

    # make ball
    ball = square.create_oval(x_start-25,y_start-25,x_start+25,y_start+25)
    square.itemconfig(ball, fill="red")

    # create next directions
    Directions = Tkinter.Label(text="Please click the direction in which"\
                               " you want Bouncy to bounce.")
    Directions.grid(row=2,column=0)
    
    square.bind("<Button-1>", get_slope)
    square.pack()

def get_mouse(event):
    global x_start,y_start
    
    #retrieve the click coordinates
    x_start = int(event.x)
    y_start = int(event.y)

    #make sure ball is preset inside the box
    if x_start < 29:
        x_start = 29
    if x_start > 473:
        x_start = 473
    if y_start < 29:
        y_start = 29
    if y_start > 473:
        y_start = 473
        
    make_start_ball()
    
# make instruction window
Instructions = Tkinter.Tk()
Instructions.title("Instructions")

Inst = Tkinter.Frame(Instructions)
Inst.grid(row=0,column=0)

Start = Tkinter.Label(text="Please click where you want Bouncy to start")
Start.grid(row=1,column=0)

# make bouncy's window
Game = Tkinter.Tk()
Game.title("Bouncy...the amazing bouncing ball!!!")

square = Canvas(Game, width=500, height=500)
square.bind("<Button-1>", get_mouse)
square.pack()

# outline box
N = square.create_line(3,3,500,3)
W = square.create_line(500,500,500,3)
E = square.create_line(3,3,3,500)
S = square.create_line(3,500,500,500)

Game.mainloop()
