###
#   This program generates a GUI for a tiebreaker
#   between two people
#
###

# global Stuff
import Tkinter,random
from Tkinter import *
ERRORS_LIST = [ ]

# error Message creator
def ERROR_MESSAGE():
  global ERRORS_LIST
  
  errors = Tkinter.Tk()
  errors.title("!!ERROR!!")

  IDK = Tkinter.Frame(errors)
  IDK.grid(row=0,column=0)

  IVI = Tkinter.Label(IDK,text="INVALID INPUT -- Please enter a valid number and "\
                                   "re-submit it ...")
  IVI.grid(row=1,column=0)
  
  ERRORS_LIST.append(errors)
  errors.mainloop()

# taking p1 input - processing it
def run_p1():
  p1_function(0)
  
def p1_function(a):
  global l
  global p1
  p1 = entry1.get()
  
  # problems w/ decimal placement
  if len(p1) == 1:
      p1[0] == '0'
      
  if len(p1) == 0:
    ERROR_MESSAGE()
    return
  
  if p1[0] == '0':
      p1 = p1[1:]
      
  # checks to see if input is valid
  if not p1.isdigit() or int(p1) < 0 or int(p1) > 100:
      ERROR_MESSAGE()
      return
  
  l = abs(My_number - int(p1))
  entry1.config(state = DISABLED)
  submit1.config(state = DISABLED)
  entry2.config(state = NORMAL)
  submit2.config(state = NORMAL)

# taking p2 input - processing it
def run_p2():
  p2_function(0)
  
def p2_function(a):
  global k
  global p2
  p2 = entry2.get()

  # problems w/ decimal placement
  if len(p2) == 1:
     p2[0] == '0'
  
  if len(p2) == 0:
    ERROR_MESSAGE()
    return
  
  if p2[0] == '0':
     p2 = p2[1:]
     
  # check =to see if it's the same number
  if p1 == p2:
      ERROR_MESSAGE()
      return
    
  # checks to see if input is valid
  if not p2.isdigit() or int(p2) < 0 or int(p2) > 100:
      ERROR_MESSAGE()
      return
  
  k = abs(My_number - int(p2))
  entry2.config(state = DISABLED)
  submit2.config(state = DISABLED)
  make_results()

# quitting all windows function
def destroy():
  global ERRORS_LIST
  results.destroy()
  game.destroy()
  
  for bob in ERRORS_LIST:
    bob.destroy()

# making the results window
def make_results():
  global results

  results = Tkinter.Tk()
  results.title("Results")

  Results = Tkinter.Frame(results)
  Results.grid(row = 0,column = 0)

  Mynumber = Tkinter.Label(Results,text = ("My number was " + str(My_number) + "."))
  Mynumber.grid(row = 0)

  #check if people guessed my number
  if int(My_number) == int(p1) or int(My_number) == int(p2):
      if int(My_number) == int(p1):
          p1guessed = Tkinter.Label(Results,text = "Player 1 guessed my number!!!", fg = 'blue')
          p1guessed.grid(row = 1)
          p1wins = Tkinter.Label(Results,text = "Player 1 Wins!!!", fg = 'blue')
          p1wins.grid(row = 2)
          Quit = Tkinter.Button(Results,text = "QUIT",command = destroy)
          Quit.grid(row = 3)
          return

      elif int(My_number) == int(p2):
          p2guessed = Tkinter.Label(Results,text = "Player 2 guessed my number!!!", fg = 'red')
          p2guessed.grid(row = 1)
          p2wins = Tkinter.Label(Results,text = "Player 2 Wins!!!", fg = 'red')
          p2wins.grid(row = 2)
          Quit = Tkinter.Button(Results,text = "QUIT",command = destroy)
          Quit.grid(row = 3)
          return
        
  Mynumber = Tkinter.Label(Results,text = ("My number was " + str(My_number) + "."))
  Mynumber.grid(row = 0)

  Quit = Tkinter.Button(Results,text = "QUIT",command = destroy)
  Quit.grid(row = 2)

            
  #calculating winner
  if l < k:
      p1wins = Tkinter.Label(Results,text = "Player 1 Wins!!!", fg = 'blue')
      p1wins.grid(row = 1)
  
  elif k < l:
      p2wins = Tkinter.Label(Results,text = "Player 2 Wins!!!", fg = 'red')
      p2wins.grid(row = 1)

  results.mainloop()
  
My_number = random.randint(1,100)
  
#main Game window
game = Tkinter.Tk()
game.title("Tiebreaker 1.0")

Window = Tkinter.Frame(game)
Window.grid(row = 0,column = 0)

Welcome = Tkinter.Label(Window,text="Welcome to Tiebreaker 1.0!")
Welcome.grid(row = 1)

IHave = Tkinter.Label(Window,text="I have picked a number between 1 and 100")
IHave.grid(row = 2)

#Player 1 stuff
prompt1 = Tkinter.Label(Window,text = "Player 1: Pick a number between 1 and 100:", fg = 'blue')
prompt1.grid(row = 3, column = 0)

entry1 = Tkinter.Entry(Window, width = 3)
entry1.grid(row = 3, column = 1)
entry1.bind("<Return>", p1_function)

submit1 = Tkinter.Button(Window,text="Submit", bg = "blue", fg = 'yellow', command = run_p1)
submit1.grid(row = 3,column = 2)


#Player 2 Stuff
prompt2 = Tkinter.Label(Window,text = "Player 2: Pick a number between 1 and 100:", fg = 'red')
prompt2.grid(row = 4,column = 0)

entry2 = Tkinter.Entry(Window, width = 3)
entry2.grid(row = 4,column = 1)
entry2.config(state = DISABLED)
entry2.bind("<Return>", p2_function)

submit2 = Tkinter.Button(Window, text = "Submit", bg = 'red', command = run_p2)
submit2.grid(row = 4, column = 2)
submit2.config(state = DISABLED)

game.mainloop()
