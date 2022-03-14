from cgitb import text
from contextlib import redirect_stderr
from itertools import cycle
from random import randrange
from tkinter import Tk, Canvas,messagebox,font
from tkinter.ttk import Style
from tracemalloc import start
from turtle import width

canvas_width= 800
canvas_hight = 400

win = Tk()
c= Canvas(win, width= canvas_width,height= canvas_hight, background= 'deep sky blue')
c.create_rectangle (-5,canvas_hight-100, canvas_width+5,canvas_hight+5,fill= 'sea green',width= 0)
c.create_oval(-80,-80,120,120, fill='orange')
c.pack()

color_cycle= cycle([' blue', 'pink', 'yellow','green','red','blue','green','black'])
egg_width = 45
egg_ghight =55
egg_score =10
egg_speed = 500
egg_interval = 4000
difficulty_color = 0.95

catcher_color = 'blue'
catcher_width= 100
catcher_hight = 100
catcher_start_x = canvas_width/2 - catcher_width/2
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y = canvas_hight - catcher_hight -20
catcher_start_y2 = catcher_start_y + catcher_hight

catcher = c.create_arc(catcher_start_x,catcher_start_y,catcher_start_x2,catcher_start_y2, start = 200, extent = 140 ,style = 'arc', outline = catcher_color,width = 3 )

score = 0
score_text = c.create_text(10, 10, anchor= 'nw', font= ('Ariel', 16, 'bold'),fill= 'darkblue',text= 'Score = '+ str(score))
lives= 3
lives_text = c.create_text(canvas_width-100, 10, anchor= 'nw', font= ('Ariel', 16, 'bold'),fill= 'darkblue',text= 'Lives = '+ str(lives))

eggs =[]

def create_eggs():
    x= randrange(10,740)
    y=40
    new_egg=c.create_oval(x,y,x+egg_width,y+egg_ghight,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2)= c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_hight:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    lose_a_life()
    if lives == 0:
        messagebox.showinfo('GAME OVER','Final Score : '+ str(score))
        win.destroy()
def lose_a_life():
    global lives
    lives -=1
    c.itemconfig(lives_text,text = 'Lives : '+ str(lives))


win.mainloop()
