#!/usr/bin/env python3
import argparse
from uuid import uuid4
from os import name, system
from random import choice, SystemRandom

parser = argparse.ArgumentParser(prog="NPass Console Option", 
formatter_class=argparse.RawDescriptionHelpFormatter, 
description="""\
    README
    To prevent your passwords from being hacked by social engineering, 
    brute force or dictionary attack method, and keep your
    online accounts safe, you should notice that

    * Always use a unique password for each account.
    * Do not use personal information in your passwords. Names, birthdays and the like.
    * Passwords must be at least 15, contain letters, numbers, symbols
    * Avoid fairly weak, and commonly used passwords
    * Do not use similar passwords that change only one word or any other character.

        2020 Wizard Packed, Free Software
        Git: https://github.com/appath/NPass""")

parser.add_argument("-v", "--version", action="version", help="print version", version="%(prog)s [version 0.2.1] 10/08/2020")
parser.add_argument("-l", dest="length", type=int, help="length of password in integer, default is [8]", default=8)
parser.add_argument("-c", dest="count", type=int, help="number of passwords to generate", default=1)
args = parser.parse_args()

def get_info():
    print(f"\nGenerate [{count}] a random string of fixed length")
    print(f"Use the sampling function when you don’t want to repeat [{length}] characters in a random")
    print("=" * 32 + "\n")

def get_passwords():
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = uuid4().hex
    SR = SystemRandom()
    return "".join(SR.choice(password_characters + salt) for i in range(length))

if __name__ == "__main__":
    try:
        length = args.length
        count = args.count

        get_info()

        for str_count in range(count):
            print(get_passwords())

        input("\nPress ENTER to exit()")
        system("cls" if name == "nt" else "clear")

    except KeyboardInterrupt:
        system("cls" if name == "nt" else "clear")
