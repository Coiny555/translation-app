from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
root['bg'] = 'pink'
root.title('Real-time translator')

Label(root, text="Language Translator", font="Arial 20 bold").pack()
 
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)
 
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)
 
language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')

root.mainloop()
