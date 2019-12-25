# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import webbrowser

# Function for copying password
def copy_set():
	pass

src = Tk()

src.wm_title("#Generate Secure Password")
src.iconbitmap("img/icon.ico")
src.resizable(height=False, width=False)
src.geometry("544x262")

#NoteBook
note = ttk.Notebook(src)

details = Frame(note)
information = Frame(note)
about = Frame(note)

note.add(details, text="  Details  ", compound=TOP)
note.add(information, text="  Information  ")
note.add(about, text="  About  ")
note.pack(fill=BOTH, expand=True)

#Details NOTE
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
generate_0 = ttk.Button(character_set2, text="Copy", command=copy_set)
generate_1 = ttk.Button(character_set2, text="Generate")
generate_0.grid(row=0, column=1)
generate_1.grid(padx=0, row=0, column=2)

#LabelFrame2 END
character_set2.pack(fill="both", expand="yes", padx=4, pady=4)

#WEB_LINK
url = "https://github.com/appath/GeneratePassword/releases"

def callback_function(event):
    webbrowser.open_new(url)

link = ttk.Label(src, text="#Releases", cursor="hand2")
link.bind("<Button-1>", callback_function)
link.pack(padx=4, side=LEFT)

#Information NOTE
#LabelFrame3
character_set3 = ttk.LabelFrame(information, text="Create strong and random passwords")

#README
readme = ttk.Label(character_set3, text="Be sure to use a unique password for each new account.\
	\nThe danger of using the same passwords is that if one site is compromised, it will\
	\nbe easier for hackers to try to use the same username and password combination on\
	\nother websites.\
	\n\
	\nDo not use any data related to your identity in passwords. Names,\
	\nbirthdays and addresses are easy to remember, but they are also\
	\neasy to find on the Internet. Therefore, to achieve maximum\
	\npassword strength, this information should not be used.\
	\n\
	\nPasswords must be at least 12 characters long and contain letters, numbers\
	\nand special characters. Try not to use weak and commonly used passwords.")
readme.grid(padx=4, row=0, column=0)

#LabelFrame3 END
character_set3.pack(fill="both", expand="yes", padx=4, pady=4)

if __name__ == "__main__":
	src.mainloop()
