#!/usr/bin/env python3
import uuid
import random
import argparse

parser = argparse.ArgumentParser(prog="NPass Console", formatter_class=argparse.RawDescriptionHelpFormatter, description="""\
    To prevent your passwords from being hacked by social engineering, 
    brute force or dictionary attack method, and keep your
    online accounts safe, you should notice that
    
    * Always use a unique password for each account.
    * Do not use personal information in your passwords. Names, birthdays and the like.
    * Passwords must be at least 15, contain letters, numbers, symbols
    * Avoid fairly weak, and commonly used passwords
    * Do not use similar passwords that change only one word or any other character.
    
    2020 Wizard Packed, Free Software
    GitHub: https://github.com/appath""")
parser.add_argument("-v", "--version", help="print version", action="version", version="%(prog)s [version 1.12.0]")
parser.add_argument("-l", dest="length", type=int, help="length of password in integer, default is 8", default=8)
parser.add_argument("-c", dest="count", type=int, help="number of passwords to generate", default=1)
(options) = parser.parse_args()
length = options.length
count = options.count

def get_password():
    salt = uuid.uuid4().hex
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(salt + password_characters) for i in range(length))

def info_password_0():
    print("Strong passwords are unique and random.\n")

def info_password_1():
    print(f"\n:: Generate {count} a random string of fixed length")
    print(f"   Use the sampling function when you don’t want to repeat {length} characters in a random . . .")

if __name__ == "__main__":
    info_password_0()
    for str_count in range(count):
        print(get_password())
    info_password_1()
