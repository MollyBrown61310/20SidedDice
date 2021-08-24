import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Mah 20 Sided Dice')
root.iconbitmap(r'dragon.ico')


# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text= "Molly's 20 Sided Dice", fg = "darkblue", 
        
        font = "Helvetica 50 bold ")
l1.pack()

# images
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png', 'dice7.png', 'dice8.png', 'dice9.png', 'dice10.png', 'dice11.png' , 'dice12.png', 'dice13.png', 'dice14.png', 'dice15.png',
 'dice16.png', 'dice17.png', 'dice18.png', 'dice19.png', 'dice20.png'  ]

# simulating the dice with random numbers between 0 to 20 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll The Dice', fg='darkblue', width=25, height=5, command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()