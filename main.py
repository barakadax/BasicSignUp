'''
|￣￣￣￣￣￣￣￣￣￣￣|
| code by Barakadax  |
|＿＿＿＿＿＿＿＿＿＿＿|
(\__/) | |
(•ㅅ•) | |
/ 　 づ'''
from functions import get_username, rand_sequence, find_in_file, hash_password
from data_functions import insert_database, show_database, delete_database

def main():
    username = get_username()
    password = ""
    for run in range(0,6):
        password += find_in_file(rand_sequence())
    password = hash_password(password[:-1])
    insert_database(username, password)
    #delete_database(2)
    rows = show_database() or []
    [print(run) for run in rows]
    #O(n)

main()
