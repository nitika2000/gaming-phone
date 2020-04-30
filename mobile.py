from tkinter import *
from functools import partial
import pygame
import random 

#-----------------------------initializers---------------------------
screen = Tk()
pygame.init()

#screen
screen.title("Gaming Mobile")
screen.geometry('200x220')
screen.resizable(False, False)
#--------------------------------Frames-------------------------------

#topframe
topframe = Frame(screen)
topframe.pack()

#topframe1
topframe1 = Frame(screen)
topframe1.pack()

#topframe2
topframe2 = Frame(screen)
topframe2.pack()

#frame1
frame1 = Frame(screen)
frame1.pack()

#frame2
frame2 = Frame(screen)
frame2.pack()

#frame3
frame3 = Frame(screen)
frame3.pack()

#frame4
frame4 = Frame(screen)
frame4.pack()

#---------------------------------Input String---------------------------------

input_string = ""
flag = 1

#--------------------------------All Functions for input-----------------------

class compute:
    def num(self, x):
        global entry1
        length = len(entry1.get())
        if(x == -1):
            entry1.insert(length, str("*"))
        elif(x == -2):
            entry1.insert(length, str("#"))
        else:
            entry1.insert(length, str(x))
        
        global input_string
        global flag
        
        if(x == 1):
            input_string = input_string + "1"
        elif(x == 2):
            input_string = input_string + "2"
        elif(x == 3):
            input_string = input_string + "3"
        elif(x == 4):
            input_string = input_string + "4"
        elif(x == 5):
            input_string = input_string + "5"
        elif(x == 6):
            input_string = input_string + "6"
        elif(x == 7):
            input_string = input_string + "7"
        elif(x == 8):
            input_string = input_string + "8"
        elif(x == 9):
            input_string = input_string + "9"
        elif(x == -1):
            flag = 0
        elif(x == -2):
            flag = 0
    def Call(self):
        global entry1
        length = len(entry1.get())
        entry1.delete(0, END)
        if(length == 10 and flag == 1):
            x = random.choice([0 , 1])
            if(x == 1):
                pygame.mixer.music.load("/./home/nitika/Desktop/python/gaming phone/gayatri-mantra-raga-1.mp3")
                pygame.mixer.music.play()
            elif(x == 0):
                pygame.mixer.music.load("/./home/nitika/Desktop/python/gaming phone/numberbusy-4topyh4v-834.mp3")
                pygame.mixer.music.play()
            self.Retry()
        else:
            entry1.insert(0, "INVALID PRESS RETRY")
    
    def Retry(self):
        global entry1
        global flag
        flag = 1
        entry1.delete(0,END)
    
    def End(self):
        screen.destroy()
#---------------------------------Show Part-----------------------------------

comp = compute()

#Name Label
label1= Label(topframe, text="Number")
label1.pack(side = TOP)

#Name Entry
entry1 = Entry(topframe1, bd = 5)
entry1.insert(0, '')
entry1.pack(side = TOP)

#call Button
button1 = Button(topframe2, text="CALL", fg="green", command=comp.Call)
button1.pack(side=LEFT)

#retry button
button1 = Button(topframe2 , text = " Retry ", command= comp.Retry)
button1.pack(side=LEFT)

#End Call
button1 = Button(topframe2, text = "END", fg="red", command= comp.End)
button1.pack(side=RIGHT)

#digit 1
button1 = Button(frame1, text=" 1 ", command=partial(comp.num , 1))
button1.pack(side= LEFT)

#digit 2
button1 = Button(frame1, text=" 2 ", command=partial(comp.num , 2))
button1.pack(side= LEFT)

#digit 3
button1 = Button(frame1, text=" 3 ", command=partial(comp.num , 3))
button1.pack(side= LEFT)

#digit 4
button1 = Button(frame2, text=" 4 ", command=partial(comp.num , 4))
button1.pack(side= LEFT)

#digit 5 
button1 = Button(frame2, text=" 5 ", command=partial(comp.num , 5))
button1.pack(side= LEFT)

#digit 6
button1 = Button(frame2, text=" 6 ", command=partial(comp.num , 6))
button1.pack(side= LEFT)

#digit 7
button1 = Button(frame3, text=" 7 ", command=partial(comp.num , 7))
button1.pack(side= LEFT)

#digit 8
button1 = Button(frame3, text=" 8 ", command=partial(comp.num , 8))
button1.pack(side= LEFT)

#digit 9
button1 = Button(frame3, text=" 9 ", command=partial(comp.num , 9))
button1.pack(side= LEFT)

#digit *
button1 = Button(frame4, text= " * ", command=partial(comp.num , -1))
button1.pack(side = LEFT)

#digit 0
button1 = Button(frame4, text= " 0 ", command=partial(comp.num , 0))
button1.pack(side = LEFT)

#digit #
button1 = Button(frame4, text= " # ", command=partial(comp.num , -2))
button1.pack(side = LEFT)

screen.mainloop()