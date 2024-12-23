from tkinter import *
import random

root = Tk()

fullscreen = True
root.attributes('-fullscreen', fullscreen)
root.geometry("400x400")  

computervalue = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"    
}

def resetgame():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player")
    l2.config(text = "Computer")
    l3.config(text = "")

def btndisable():
    b1["state"] = "disable"
    b2["state"] = "disable"  
    b3["state"] = "disable"  

def isrock():
    cv = computervalue[str(random.randint(0, 2))]
    if cv == "Rock":
        match_result = "Match Draw"
    elif cv == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text = match_result)
    l1.config(text = "Rock     ")
    l2.config(text = cv)
    btndisable()

def ispaper():
    cv = computervalue[str(random.randint(0, 2))]
    if cv == "Paper":
        match_result = "Match Draw"
    elif cv == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l3.config(text = match_result)
    l1.config(text = "Paper     ")
    l2.config(text = cv)
    btndisable()

def isscissor():
    cv = computervalue[str(random.randint(0, 2))]
    if cv == "Rock":
        match_result = "Computer Win"
    elif cv == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l3.config(text = match_result)
    l1.config(text = "Scissor     ")
    l2.config(text = cv)
    btndisable()

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        root.attributes('-fullscreen', True)
    else:
        root.attributes('-fullscreen', False)
        root.geometry("400x400")  


frame = Frame(root)
frame.pack(pady=10)

l1 = Label(frame, text = "Player           ", font = ("Arial", 12), bg = "#83a4ab", fg = "white")
l2 = Label(frame, text = "VS           ", font = ("Arial", 12, "bold"), bg = "#a0b9be", fg = "white")
l3 = Label(frame, text = "Computer           ", font = ("Arial", 12), bg = "#acbbbe", fg = "white")

l1.pack(side = LEFT, padx=10)
l2.pack(side = LEFT, padx=10)
l3.pack(side = LEFT, padx=10)


l4 = Label(root, text = "", font = ("Arial", 20, "bold"), bg = "#bdd7dd", fg = "white", width = 20, borderwidth = 2, relief = "solid")
l4.pack(pady = 20)


frame1 = Frame(root)
frame1.pack(pady=10)

b1 = Button(frame1, text = "Rock", font = ("Arial", 12), fg = "white", bg = "#188eac", width = 10, command = isrock)
b2 = Button(frame1, text = "Paper", font = ("Arial", 12), fg = "white", bg = "#34899e", width = 10, command = ispaper)
b3 = Button(frame1, text = "Scissor", font = ("Arial", 12), fg = "white", bg = "#4d7c87", width = 10, command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b3.pack(side = LEFT, padx = 10)


Button(root, text = "Reset Game", font = ("Arial", 12), fg = "white", bg = "#3c7684", command = resetgame).pack(pady = 20)
Button(root, text="Toggle Fullscreen", fg = "white", bg = "#91d6e7", command=toggle_fullscreen).pack(pady=10)

root.bind('<F11>', toggle_fullscreen)

root.mainloop()


    
    