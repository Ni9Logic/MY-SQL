import os
import time
import msvcrt as m
import mysql.connector
import signinpage as sp
from datetime import datetime
from re import I

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

class NewUser:
    created = datetime.now()
    new_user_name = "0"
    new_user_age = 0
    new_user_pass = "0"
    new_user_Account_Type = "0"
    new_user_BankBal = "0"

    def new_user_createaccount(self):
            os.system("cls||clear")
            select_query = "SELECT * FROM user WHERE name=%s"
            self.new_user_name = "0"
            if self.new_user_name == "0" or len(self.new_user_name) == 0:
                while self.new_user_name == "0" or len(self.new_user_name) == 0:
                    self.new_user_name = input("\t\t\tEnter\u001b[1;31m Username\u001b[1;0m: ")
            database.execute(select_query, (self.new_user_name,))
            if database.fetchall():
                print("\t\t\tUser Alreasdy Exists")
                print("\t\t\tPress Any key to continue...")
                m.getch()
            else:
                self.created = datetime.now()
                self.new_user_age = "0"
                if self.new_user_age == "0" or len(self.new_user_age) == 0 or not self.new_user_age.isdigit():
                    while self.new_user_age == "0" or len(self.new_user_age) == 0 or not self.new_user_age.isdigit():
                        self.new_user_age = input("\t\t\tEnter\u001b[1;31m Age\u001b[1;0m: ")
                self.new_user_pass = "0"
                if self.new_user_pass == "0" or len(self.new_user_pass) == 0:
                    while self.new_user_pass == "0" or len(self.new_user_pass) == 0:
                        self.new_user_pass = input("\t\t\tEnter\u001b[1;31m Password\u001b[1;0m For User: ")
                self.new_user_BankBal = "0"
                if self.new_user_BankBal == "0" or len(self.new_user_BankBal) == 0 or not self.new_user_BankBal.isdigit():
                    while self.new_user_BankBal == "0" or len(self.new_user_BankBal) == 0 or not self.new_user_BankBal.isdigit():
                        self.new_user_BankBal = input("\t\t\tEnter\u001b[1;31m Initial_Deposit\u001b[1;0m For User: ")
                print("\t\t\tThere are \u001b[1;31mTwo Types\u001b[1;0m of Banking Accounts\n\t\t\t1 \u001b[1;31m-->\u001b[1;0m Savings \n\t\t\t2 \u001b[1;31m-->\u001b[1;0m Current")
                self.new_user_Account_Type = "0"
                if self.new_user_Account_Type == "0" or len(self.new_user_Account_Type) == 0:
                    while self.new_user_Account_Type == "0" or len(self.new_user_Account_Type) == 0:
                        self.new_user_Account_Type = input("\t\t\tEnter\u001b[1;31m Account_Type\u001b[1;0m For User: ")
                        if self.new_user_Account_Type == "1":
                            self.new_user_Account_Type = "Savings"
                        elif self.new_user_Account_Type == "2":
                            self.new_user_Account_Type = "Current"
                print("\t\t\tAccount \u001b[1;31mSuccessfully Created\u001b[1;0m\n\t\t\tPress Any Key to continue")
                m.getch()
                # Uploading into database
                database.execute("INSERT INTO User (created, name, age, password, bankbal, account_Type) VALUES(%s, %s, %s, %s, %s, %s)", (self.created, self.new_user_name, self.new_user_age, self.new_user_pass, self.new_user_BankBal, self.new_user_Account_Type))
                db.commit()