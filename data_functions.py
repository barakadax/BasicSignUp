'''
|￣￣￣￣￣￣￣￣￣￣￣|
| code by Barakadax  |
|＿＿＿＿＿＿＿＿＿＿＿|
(\__/) | |
(•ㅅ•) | |
/ 　 づ'''
from sqlite3 import connect
from datetime import date

def insert_database(username, password):    #Add new user into the table, auto PK ID
    try:
        with connect(r"diceware_exercise.db") as conn:
            rows = conn.execute("SELECT * FROM accounts")
            count = 1
            for check in rows:
                count -= -1
            conn.execute("INSERT INTO accounts(account_id, username, password, register_date) VALUES (?, ?, ?, ?)", (count, username, password, date.today()))
    except Error as error:
        print("Error while connecting to sqlite: ", error)
    #O(N)

def show_database():    #Returns all users from the table
    try:
        with connect(r"diceware_exercise.db") as conn:
            return conn.execute("SELECT * FROM accounts")
    except Error as error:
        print("Error while connecting to sqlite: ", error)
        return None
    #O(1)

def delete_database(id_num):    #Delete user from the table by ID
    whom = "DELETE FROM accounts WHERE account_id = " + str(id_num)
    try:
        with connect(r"diceware_exercise.db") as conn:
            conn.execute(whom)
    except Error as error:
        print("Error while connecting to sqlite: ", error)
    #O(1)
