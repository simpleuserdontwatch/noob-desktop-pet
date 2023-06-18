'''
Noob - desktop pet
By: SimpleUserDontWatch
'''
from PIL import Image, ImageTk
import tkinter as tk
import time,random,keyboard
import pyautogui,sys,subprocess,threading
from tkinter import messagebox
pyautogui.PAUSE = 0

dialogs = ["i am out of mind what to do","i wanna show you somethin'",
           "epik.","y' know what, i am bored"
           ,"can i eat?","i dont know what to do"
           ,"grrrrrrrrr","that thing on your screen..... looks creppy for me"]

root = tk.Tk()

# Load the image file
img = Image.open("smile.png")

photo = ImageTk.PhotoImage(img)
# Make bouncing physics
w,h = pyautogui.size()
if random.randint(0,1) == 1:
    xvel = 1
else:
    xvel = -1
if random.randint(0,1) == 1:
    yvel = 1
else:
    yvel = -1
x,y = random.randint(0,w-64),random.randint(0,h-64)
w-=64
h-=64
def annoy():
    pyautogui.moveTo(x,y)
    root.after(20000,annoy)
def say():
    threading.Thread(target=lambda: messagebox.showinfo('Noob',random.choice(dialogs))).start()
    root.after(15000,say)
def bounce():
    global w,h,xvel,yvel,x,y,w,h
    if random.randint(0,500) == 0:
        if random.randint(0,1) == 1:
            xvel = 1
        else:
            xvel = -1
        if random.randint(0,1) == 1:
            yvel = 1
        else:
            yvel = -1
    x+=round(xvel)
    y+=round(yvel)
    if x >= w or x <= 0:
        if xvel > 0:
            xvel+=0.05
        else:
            xvel-=0.05
        xvel*=-1
    if y >= h or y <= 0:
        if yvel > 0:
            yvel+=0.05
        else:
            yvel-=0.05
        yvel*=-1
    root.geometry(f'64x64+{x}+{y}')
    if keyboard.is_pressed('p'):
        root.destroy()
        exit()
    root.after(5,bounce)
# Create the Label widget
label = tk.Label(root, image=photo, bg='white', font=["Comic Sans MS", 30])

# Set window properties
root.overrideredirect(True)
root.geometry("+0+0")
root.config(bg='white')
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")


# Run bouncing physics
bounce()
annoy()
root.after(5000,say)
# Pack the Label widget and run the mainloop
label.pack()
messagebox.showinfo('Noob','hallo')
root.mainloop()
