# -*- coding: utf-8 -*-
#!/usr/src/env python3
import random
import pyperclip
from tkinter import *
from tkinter import ttk

# Program title and version
name = "Npass (Generate random password) | "
version = "ver.1.2.1.build.0"

# Window TK
root = Tk()
root.wm_title(f"{name} {version}")
root.iconbitmap("IDI_APPICON.ico")
root.resizable(height=False, width=False)
root.geometry("544x210")

# From which items you want to generate pass
set_check0 = IntVar()
set_check1 = IntVar()
set_check2 = IntVar()
set_check3 = IntVar()
set_combobox = IntVar()

# Items used to generate pass
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numerals_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sumbols_case = ["!", "#", "$", "/", "@", "%", "(", "&", "*", ")"]

def generate():
    exhaust.delete(0, END)

    final_list = []
    length = set_combobox.get()

    if (set_check3.get()):
        final_list.append(sumbols_case)
    if (set_check2.get()):
        final_list.append(numerals_case)
    if (set_check1.get()):
        final_list.append(lower_case)
    if (set_check0.get()):
        final_list.append(upper_case)
    
    bound = set_check0.get() + set_check1.get() + set_check2.get() + set_check3.get()

    if not (bound):
        return ("Choose the option you need . . .")
    
    password = []
    
    for i in range(length):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))

    return ("".join(password))

def display():
    password = generate()
    exhaust.insert(0, password)

def buffer():
    exhaust_pass = exhaust.get()
    pyperclip.copy(exhaust_pass)

# START
character_set0 = ttk.LabelFrame(root, text=" Character Set ")
chek_button_lower = ttk.Checkbutton(character_set0, text="Upper case (A-Z)", variable=set_check0, onvalue=1, offvalue=0)
chek_button_lower.grid(padx=4, row=0, column=0)
chek_button_upper = ttk.Checkbutton(character_set0, text="Lower case (a-z)", variable=set_check1, onvalue=1, offvalue=0)
chek_button_upper.grid(padx=4, row=0, column=1)
chek_button_numerals = ttk.Checkbutton(character_set0, text="Numerals (0-9)", variable=set_check2, onvalue=1, offvalue=0)
chek_button_numerals.grid(padx=4, row=0, column=2)
chek_button_sumbols = ttk.Checkbutton(character_set0, text="Specials sumbols (e.g !#$/@)", variable=set_check3, onvalue=1, offvalue=0)
chek_button_sumbols.grid(padx=4, row=0, column=3)
text = ttk.Label(character_set0, text="A character set is a table that specifies the encoding of a finite set of characters in the alphabet.")
text.grid(padx=4, row=1, column=0, columnspan=4, sticky=W)
character_set0.pack(fill="both", expand="yes", padx=4, pady=4)

character_set1 = ttk.LabelFrame(root, text=" Minimal Amount ")
# The text field is not editable and the user can only select values from the drop down list.
comboExample = ttk.Combobox(character_set1, values=["8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"], state="readonly", textvariable=set_combobox)
comboExample.current(0)
comboExample.bind("<<ComboboxSelected>>")
comboExample.grid(padx=6, pady=4, row=0, column=0)
text = ttk.Label(character_set1, text="Minimum length of numbers, letters and characters in a password.")
text.grid(row=0, column=1)
character_set1.pack(fill="both", expand="yes", padx=4, pady=4)

character_set2 = ttk.LabelFrame(root, text=" Secure Password ")
exhaust = ttk.Entry(character_set2, state=NORMAL, width=59)
exhaust.grid(padx=6, pady=4, row=0, column=0)
generate_0 = ttk.Button(character_set2, text="Copy", command=buffer)
generate_1 = ttk.Button(character_set2, text="Generate", command=display)
generate_0.grid(row=0, column=1)
generate_1.grid(padx=0, row=0, column=2)
character_set2.pack(fill="both", expand="yes", padx=4, pady=4)
# THE END

if __name__ == "__main__":
    root.mainloop()
