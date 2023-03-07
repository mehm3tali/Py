import keyboard
import random
import string
import time 


length = int( input( '\n Enter the desired password length: ' ))



if length == 0:
    print("Password length cannot be 0 characters!")
else : pass
use_symbols = True
use_numbers = True
use_special_characters = True

characters = string.ascii_letters
if use_numbers:
    characters += string.digits
if use_special_characters:
    characters += "?!*"

passwords = []

filename = "passwords.txt"
mode = "a"

start_number = 1

for i in range(5):
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if password not in passwords:
            passwords.append(password)
            break

    number = start_number + i

    with open(filename, mode) as file:
        file.write(f"{number}. {password}\n")
    print(f"{number}. Your passwords are saved in the passwords.txt file.")

    print ("Press ESC to exit")
    if keyboard.is_pressed('esc'):
        print("rogram is closing ")
        break


               
