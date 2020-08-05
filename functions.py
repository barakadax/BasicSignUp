'''
|￣￣￣￣￣￣￣￣￣￣￣|
| code by Barakadax  |
|＿＿＿＿＿＿＿＿＿＿＿|
(\__/) | |
(•ㅅ•) | |
/ 　 づ'''
import os
import random
import hashlib

def get_username():     #Make user type a valid input for username
    username = ""
    while (len(username) < 8):
        os.system('cls' if os.name == 'nt' else 'clear')
        username = input("Please enter a username: ").strip()
        if (len(username) < 8):
            print("Invalid username, please try again.")
        else:
            return username
    #O(n)


def rand_sequence():    #Random 5 digits & retuns a connected number
    password = 0
    for run in range(0, 5):
        password += random.randint(1, 6)
        password *= 10
    return int(password / 10)
    #O(n)


def find_in_file(find):     #Gets 5 digits number & search its value in diceware file
    with open("diceware.txt", 'r') as diceware:
        for num, line in enumerate(diceware, 1):
            if str(find) in line:
                return line.split("\n")[0][6:] + " "
    #O(n)


def hash_password(password):    #Gets string variable, returns encrypted string
    password = bytearray(password, "utf-8")
    encrypt = hashlib.sha256(password)
    return encrypt.hexdigest()
    #O(1)
