# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import webbrowser

src = Tk()

src.wm_title("#Generate Secure Password")
src.iconbitmap("img/icon.ico")
src.resizable(height=False, width=False)
src.geometry("544x255")

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
text = ttk.Label(character_set, text="A character set is a table that specifies the encoding\
	\nof a finite set of characters in the alphabet.")
text.grid(padx=4, row=1, column=0, columnspan=4, sticky=W)

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
								"24", "25", "26", "27",
								"28", "29", "30", "31",
								"32"])

comboExample.current(0) 
comboExample.bind("<<ComboboxSelected>>") 
comboExample.grid(padx=6, pady=4, row=0, column=0)

#Label1
text = ttk.Label(character_set1, text="Minimum length of numbers, letters and characters in a password")
text.grid(row=0, column=1)

#LabelFrame1 END
character_set1.pack(fill="both", expand="yes", padx=4, pady=4)

#LabelFrame2
character_set2 = ttk.LabelFrame(details, text=" Secure Password ")

#Entry password
exhaust = ttk.Entry(character_set2, width=59)
exhaust.grid(padx=6, pady=4, row=0, column=0)

#Button 0 and 1 (Copy, Generate)
generate_0 = ttk.Button(character_set2, text="Copy")
generate_1 = ttk.Button(character_set2, text="Generate")
generate_0.grid(row=0, column=1)
generate_1.grid(padx=2, row=0, column=2)

#LabelFrame2 END
character_set2.pack(fill="both", expand="yes", padx=4, pady=4)

#WEB_LINK Sub-shelf
url = "https://github.com/appath/GeneratePassword/releases"

def callback_function(event):
    webbrowser.open_new(url)

link = ttk.Label(src, text="#Releases", cursor="hand2")
link.bind("<Button-1>", callback_function)
link.pack(padx=4, side=LEFT)

if __name__ == "__main__":
	src.mainloop()

