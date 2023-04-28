import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
import time
import sys

Fg = "gray"
Bg = random.choice(["lime","blue","purple","salmon"])

TTT = tk.Tk()
TTT.title("TİC-TAC-TOE")
TTT.minsize(300,450)
TTT.maxsize(300,450)

KEY = 1

def CLEAR():
    global KEY
    KEY = 1
    PLACE_1["state"] = "normal"
    PLACE_2["state"] = "normal"
    PLACE_3["state"] = "normal"
    PLACE_4["state"] = "normal"
    PLACE_5["state"] = "normal"
    PLACE_6["state"] = "normal"
    PLACE_7["state"] = "normal"
    PLACE_8["state"] = "normal"
    PLACE_9["state"] = "normal"
    PLACE_1["text"] = ""
    PLACE_2["text"] = ""
    PLACE_3["text"] = ""
    PLACE_4["text"] = ""
    PLACE_5["text"] = ""
    PLACE_6["text"] = ""
    PLACE_7["text"] = ""
    PLACE_8["text"] = ""
    PLACE_9["text"] = ""
    

def GAMERESOULT():
    player_x_name = PLAYER_X_NAME_E.get()
    player_y_name = PLAYER_Y_NAME_E.get()
    
    if PLACE_1["text"] == "X" and PLACE_2["text"] == "X" and PLACE_3["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_4["text"] == "X" and PLACE_5["text"] == "X" and PLACE_6["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_7["text"] == "X" and PLACE_8["text"] == "X" and PLACE_9["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_1["text"] == "X" and PLACE_4["text"] == "X" and PLACE_7["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_2["text"] == "X" and PLACE_5["text"] == "X" and PLACE_8["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_3["text"] == "X" and PLACE_6["text"] == "X" and PLACE_9["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_1["text"] == "X" and PLACE_5["text"] == "X" and PLACE_9["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_3["text"] == "X" and PLACE_5["text"] == "X" and PLACE_7["text"] == "X":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_x_name+"\n"+"WİN THE GAME")
        CLEAR()


    if PLACE_1["text"] == "O" and PLACE_2["text"] == "O" and PLACE_3["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_4["text"] == "O" and PLACE_5["text"] == "O" and PLACE_6["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_7["text"] == "O" and PLACE_8["text"] == "O" and PLACE_9["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_1["text"] == "O" and PLACE_4["text"] == "O" and PLACE_7["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_2["text"] == "O" and PLACE_5["text"] == "O" and PLACE_8["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_3["text"] == "O" and PLACE_6["text"] == "O" and PLACE_9["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_1["text"] == "O" and PLACE_5["text"] == "O" and PLACE_9["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

    if PLACE_3["text"] == "O" and PLACE_5["text"] == "O" and PLACE_7["text"] == "O":
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON",player_y_name+"\n"+"WİN THE GAME")
        CLEAR()

def B1():
    global KEY
    if KEY == 1:
        PLACE_1["text"] = "X"
        PLACE_1["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_1["text"] = "O"
        PLACE_1["state"] = "disabled"
        KEY = 1
        
    GAMERESOULT()
    return 0

def B2():
    global KEY
    if KEY == 1:
        PLACE_2["text"] = "X"
        PLACE_2["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_2["text"] = "O"
        PLACE_2["state"] = "disabled"
        KEY = 1
        
    GAMERESOULT()
    return 0

def B3():
    global KEY
    if KEY == 1:
        PLACE_3["text"] = "X"
        PLACE_3["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_3["text"] = "O"
        PLACE_3["state"] = "disabled"
        KEY = 1
        
    GAMERESOULT()
    return 0

def B4():
    global KEY
    if KEY == 1:
        PLACE_4["text"] = "X"
        PLACE_4["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_4["text"] = "O"
        PLACE_4["state"] = "disabled"
        KEY = 1
    
    GAMERESOULT()
    return 0

def B5():
    global KEY
    if KEY == 1:
        PLACE_5["text"] = "X"
        PLACE_5["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_5["text"] = "O"
        PLACE_5["state"] = "disabled"
        KEY = 1

    GAMERESOULT()
    return 0

def B6():
    global KEY
    if KEY == 1:
        PLACE_6["text"] = "X"
        PLACE_6["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_6["text"] = "O"
        PLACE_6["state"] = "disabled"
        KEY = 1

    GAMERESOULT()
    return 0

def B7():
    global KEY
    if KEY == 1:
        PLACE_7["text"] = "X"
        PLACE_7["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_7["text"] = "O"
        PLACE_7["state"] = "disabled"
        KEY = 1
        
    GAMERESOULT()
    return 0

def B8():
    global KEY
    if KEY == 1:
        PLACE_8["text"] = "X"
        PLACE_8["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_8["text"] = "O"
        PLACE_8["state"] = "disabled"
        KEY = 1

    GAMERESOULT()
    return 0

def B9():
    global KEY
    if KEY == 1:
        PLACE_9["text"] = "X"
        PLACE_9["state"] = "disabled"
        KEY = 0
    
    elif KEY == 0:
        PLACE_9["text"] = "O"
        PLACE_9["state"] = "disabled"
        KEY = 1

    GAMERESOULT()
    return 0

PLAYER_X_NAME_İ = tk.Label(TTT,text = "PLAYER(X):",fg = "lime",bg = "black",font = "Arial 13")
PLAYER_X_NAME_İ.place(width = 100,height = 50,x = 0,y = 0)

PLAYER_Y_NAME_İ = tk.Label(TTT,text = "PLAYER(Y):",fg = "lime",bg = "black",font = "Arial 13")
PLAYER_Y_NAME_İ.place(width = 100,height = 50,x = 0,y = 50)

PLAYER_X_NAME_E = tk.Entry(TTT,fg = "lime",bg = "black",font = "Arial 20")
PLAYER_X_NAME_E.place(width = 200,height = 50,x = 100,y = 0)

PLAYER_Y_NAME_E = tk.Entry(TTT,fg = "lime",bg = "black",font = "Arial 20")
PLAYER_Y_NAME_E.place(width = 200,height = 50,x = 100,y = 50)

PLACE_1 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B1)
PLACE_1.place(width = 100,height = 100,x = 0,y = 100)

PLACE_2 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B2)
PLACE_2.place(width = 100,height = 100,x = 100,y = 100)

PLACE_3 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B3)
PLACE_3.place(width = 100,height = 100,x = 200,y = 100)

PLACE_4 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B4)
PLACE_4.place(width = 100,height = 100,x = 0,y = 200)

PLACE_5 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B5)
PLACE_5.place(width = 100,height = 100,x = 100,y = 200)

PLACE_6 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B6)
PLACE_6.place(width = 100,height = 100,x = 200,y = 200)

PLACE_7 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B7)
PLACE_7.place(width = 100,height = 100,x = 0,y = 300)

PLACE_8 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B8)
PLACE_8.place(width = 100,height = 100,x = 100,y = 300)

PLACE_9 = tk.Button(TTT,fg = Fg,bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 85",command = B9)
PLACE_9.place(width = 100,height = 100,x = 200,y = 300)

RESET_BUTTON = tk.Button(TTT,fg = Fg,text = "CLEAR",bg = Bg,activebackground = Bg,activeforeground = Fg,font = "Arial 35",command = CLEAR)
RESET_BUTTON.place(width = 300,height = 50,x = 0,y = 400)

TTT.mainloop() 
