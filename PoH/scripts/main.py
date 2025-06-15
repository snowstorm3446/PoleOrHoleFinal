import tkinter as tk
import PIL
import random
import os
from tkinter import ttk
from PIL import ImageTk, Image

panel = None
cgend = None
score = 0
scoreper = 'YOU HAVE PLAYED 0 ROUNDS, YOUR CURRENT ACCURACY IS N/a'
rounds = 0
gender = None
curimg = None 
# Create the main window
def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

def close_window():
    root.destroy()

root = tk.Tk()
root.title('PoH')
root.overrideredirect(True)  # Remove the default title bar
root.geometry('600x400')
root.resizable(False,False)
root.iconbitmap('Icons/Logo.ico')
root.configure(bg="black")


# Create a custom title bar
title_bar = tk.Frame(root, bg="black", relief="raised", bd=3)
title_bar.pack(side="top", fill="x")

# Add a title label
title_label = tk.Label(title_bar, bg="black", fg="white")
title_label.pack(side="left", padx=10)

# Add a close button
close_button = tk.Button(title_bar, text="X", bg="magenta", fg="white", command=close_window)
close_button.place(x=575,y=0,width=20, height=20)
#logo
img2 = ImageTk.PhotoImage(Image.open('Icons\Logo.ico'))
panel = tk.Label(root, image = img2, bg='black')
panel.place(x=3,y=3,width=20, height=20)
# Bind the title bar to allow dragging the window
title_bar.bind("<B1-Motion>", move_window)
# place a label on the root window
message = tk.Label(root, text="DOES THIS HAVE A POLE OR A HOLE?", fg='magenta', bg='black')
message.place(x=150,y=55,width=300, height=10)



#new img def
def newimg():
    global cegend, panel, img, gender, curimg, score, rounds, scoreper
    print('newimg')
    gender = random.choice(['m','f'])
    if gender == 'm':
        curimg = 'imagesP/'+random.choice(os.listdir("imagesP"))
        print(curimg)
    else:
        curimg = 'imagesH/'+random.choice(os.listdir("imagesH"))
        print(curimg)
    
    img = ImageTk.PhotoImage(Image.open(curimg))
    panel = tk.Label(root, image = img, bg='black')
    panel.place(x=150,y=75,width=300, height=200)
    #calc score
    if rounds == 0 or score == 0:
        scoreper = 'YOU HAVE PLAYED '+str(rounds)+' ROUNDS, YOUR CURRENT ACCURACY IS '+str(round(((score+0.001)/(rounds+0.001))*100))+'%'+' ('+str(score)+'/'+str(rounds)+')'
    else:
        scoreper = 'YOU HAVE PLAYED '+str(rounds)+' ROUNDS, YOUR CURRENT ACCURACY IS '+str(round((score/rounds)*100))+'%'+' ('+str(score)+'/'+str(rounds)+')'
    #display score
    scoredisplay = tk.Label(root, text =scoreper, fg='magenta', bg='black')
    scoredisplay.place(x=50,y=275 ,width=500, height=25)
#first image
newimg()


#buttons
def pole():
    global gender, score, rounds
    if gender == 'm':
        print('correct')
        score +=1
    else:
        print('incorrect')
    rounds +=1
    newimg()
    # do something to judge of it was a pole?
    # update score?
    # display new image?

def hole():
    global gender, score, rounds
    if gender == 'f':
        print('correct')
        score +=1
    else:
        print('incorrect')
    rounds +=1
    newimg()
    # do something to judge of it was a hole?
    # update score?
    # display new image?



#actual buttons
button = tk.Button(
   root, 
   text="POLE", 
   bg='black',
   fg='magenta',
   command=pole
)
button.place(x=0,y=300,width=300, height=100)
button = tk.Button(
   root, 
   text="HOLE",
   bg='black',
   fg='magenta',
   command=hole
)
button.place(x=300,y=300,width=300, height=100)


# keep the window displaying
root.mainloop()
