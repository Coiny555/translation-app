from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import os
import numpy as np
from PIL import ImageTk, Image, ImageEnhance
from pygame import *
import time



#create GUI object (Tk)
root = Tk()
root.geometry('1100x320') # When initally opening the object, the size of the length and with
root.resizable(True, True) # Shows if the user can minimize the length and/or width
root['bg'] = 'RED' # Color of the background font
root.title('Kenyon Real-Time Translator') # Name of the tab 

#"Label()" adds text to the GUI and "place()" places it.
Label(root, text="Language Translator", font="Arial 20 bold").pack()
#.pack() is the center?
 
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)

mixer.init() #Mixer is how you can use and play sounds
v = mixer.Sound('Vine Boom.mp3') # Puts the sound in the application

def fade_in(image_label, img, steps=50, delay=50):
    for i in range(steps + 1):
        LightUp = i / float(steps)
        ImgWLight = ImageEnhance.Brightness(img).enhance(LightUp)
        UpdatedImg = ImageTk.PhotoImage(ImgWLight)
        image_label.config(image=UpdatedImg)
        image_label.image = UpdatedImg
        root.update()
        time.sleep(delay / 2000)


def fade_out(image_label, img, steps=50, delay=50):
    for i in range(steps + 1):
        BlackOut = (steps - i) / float(steps)
        ImgDark = ImageEnhance.Brightness(img).enhance(BlackOut)
        UpdatedImg = ImageTk.PhotoImage(ImgDark)
        image_label.config(image=UpdatedImg)
        image_label.image = UpdatedImg
        root.update()
        time.sleep(delay / 2000)




img = Image.open('L.jpg')

nimg = img.resize((130,130), Image.LANCZOS)

nimg.save('L2.jpg')

img2 = ImageTk.PhotoImage(nimg)


image_label = Label(root, image=img2)












Input_text = Entry(root, width=60) # Entry() shows you entering the text in a box
Input_text.place(x=30, y=130)
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50) # Text() shows texts that will appear
Output_text.place(x=600, y=130)

 
language = list(LANGUAGES.values()) # Shows all the languages
dest_lang = ttk.Combobox(root, values=language, width=20) # size of the "Enter language" box. Clickable.
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')

def Translate(): # This function shows to be able to reanslate your text into another language
    try:
        translator = Translator() # Creates translation object
        translation = translator.translate(Input_text.get(), dest=dest_lang.get()) # Gets the translation text and the set language
        Output_text.delete(1.0, END) # Deletes the current text in the output box
        Output_text.insert(END, translation.text) # Inserts the output language from the input text.
        
    except Exception as e:
        print(f"Translation error: {e}") # If no language is detected, then throw an error.
        Output_text.delete(1.0, END)
        v.play() #Plays the sound from mixer
        image_label.place(x = 430, y = 40)
        fade_in(image_label, nimg)
        fade_out(image_label, nimg)
        image_label.config(image = '')
        image_label.place(x = -700, y = 200)
        


trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180) # Adds a clickable button for translation.


root.mainloop() #makes/keeps the application running


