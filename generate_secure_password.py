# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import webbrowser

src = Tk()

src.title("#Generate Secure Password")
src.iconbitmap("img/icon.ico")
src.resizable(height=False, width=False)
src.geometry("544x230")

#NoteBook
note = ttk.Notebook(src)

details = Frame(note)
information = Frame(note)
about = Frame(note)

note.add(details, text="  Details  ", compound=TOP)
note.add(information, text="  Information  ")
note.add(about, text="  About  ")
note.pack(fill=BOTH, expand=True)

#LabelFrame 
character_set = ttk.LabelFrame(details, text=" Character Set ")

#Checkbutton
check_button1 = IntVar()
chek_button_lower = ttk.Checkbutton(character_set, text="Upper case (A-Z)", variable=check_button1)
#Tk_Checkbutton(selectcolor="#f0f0f0") Color to use for the selector.
chek_button_lower.grid(padx=4, row=0, column=0)

check_button2 = IntVar()
chek_button_upper = ttk.Checkbutton(character_set, text="Lower case (a-z)", variable=check_button2)
chek_button_upper.grid(padx=4, row=0, column=1)

check_button3 = IntVar()
chek_button_numerals = ttk.Checkbutton(character_set, text="Numerals (0-9)", variable=check_button3)
chek_button_numerals.grid(padx=4, row=0, column=2)

check_button4 = IntVar()
chek_button_sumbols = ttk.Checkbutton(character_set, text="Specials sumbols (e.g !#$/@)", variable=check_button4)
chek_button_sumbols.grid(padx=4, row=0, column=3)

#Label
text = ttk.Label(character_set, text="A character set is a table that specifies the encoding of a finite set of characters in the alphabet.")
text.grid(row=1, columnspan=4)

#LabelFrame END
character_set.pack(fill="both", expand="yes", padx=4, pady=4)

#LabelFrame1
character_set1 = ttk.LabelFrame(details, text=" Minimal Amount ")

#Combobox
comboExample = ttk.Combobox(character_set1, 
                            values=[
                            		"8", "9", "10", "11", 
                            		"12", "13", "14", "15", 
                            		"16", "17", "18", "19", 
                            		"20", "21", "22", "23", 
                            		"24", "25", "26", "27",])

comboExample.current(0) 
comboExample.bind("<<ComboboxSelected>>") 
comboExample.grid(padx=6, pady=4, row=0, column=0)

#Label1
text = ttk.Label(character_set1, text="Minimum length of numbers, letters and characters in a password")
text.grid(row=0, column=1)

#LabelFrame1 END
character_set1.pack(fill="both", expand="yes", padx=4, pady=4)


#Entry password
#exhaust = Entry(details, width=35)
#exhaust.pack()

#Button
#generate = ttk.Button(details, text="Generate")
#generate.pack()

#WEB_LINK
url = "https://github.com/appath/GeneratePassword"

def callback_function(event):
    webbrowser.open_new(url)

link = ttk.Label(src, text="#Releases", cursor="hand2")
link.pack(padx=4, side=LEFT)
link.bind("<Button-1>", callback_function)

if __name__ == "__main__":
	src.mainloop()
