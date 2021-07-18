import os
import time
import msvcrt as m
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

class SignInPage:
    user_choice = "1"
    admin_name = "0"
    admin_pass = "0"
    user_name = "0"
    user_pass = "0"
    Logged = False
    def login(self):
        os.system("cls||clear")
        print("\t\t\tWelcome to \u001b[1;31mSUNUDSS KA BANK! HAHAHA MERA BANK\u001b[1;0m")
        print("\t\t\t1 \u001b[1;31m-->\u001b[1;0m Sign in as admin")
        print("\t\t\t2 \u001b[1;31m-->\u001b[1;0m Sign in as user")
        print("\t\t\t3 \u001b[1;31m-->\u001b[1;0m Create a New Account")
        print("\t\t\t4 \u001b[1;31m-->\u001b[1;0m Exit")
        self.user_choice = str(input("\t\t\tEnter: "))
        if self.user_choice == "0" or self.user_choice > "4" or len(self.user_choice) == 0:
            while self.user_choice == "0" or self.user_choice > "4" or len(self.user_choice) == 0:
                os.system("cls||clear")
                print("\t\t\tYou've Entered Incorrect Statement.")
                os.system("cls||clear")
                print("\t\t\tWelcome to \u001b[1;31mSUNUDSS KA BANK! HAHAHA MERA BANK\u001b[1;0m")
                print("\t\t\t1 \u001b[1;31m-->\u001b[1;0m Sign in as admin")
                print("\t\t\t2 \u001b[1;31m-->\u001b[1;0m Sign in as user")
                print("\t\t\t3 \u001b[1;31m-->\u001b[1;0m Create a New Account")
                print("\t\t\t4 \u001b[1;31m-->\u001b[1;0m Exit")
                self.user_choice = input("\t\t\tEnter Again: ")
                self.user_choice = str(self.user_choice)
        return self.user_choice
    def adminlogin(self):
        os.system("cls||clear")
        self.admin_name = input("\t\t\tEnter \u001b[1;31mUsername\u001b[1;0m: ")
        self.admin_pass = input("\t\t\tEnter \u001b[1;31mPassword\u001b[1;0m: ")
        if self.admin_name == "admin" and self.admin_pass == "admin":
            os.system("cls||clear")
            print("\t\t\tYou've Successfully \u001b[1;31mlogged\u001b[1;0m in as an \u001b[1;31madministrator\u001b[1;0m...")
            time.sleep(1)
            SignInPage.Logged = True
        else:
            os.system("cls||clear")
            print("\t\t\t\u001b[1;31mNOTE:\u001b[1;0m You've entered incorrect \u001b[1;31mCredentials\u001b[1;0m")
            print("\t\t\tForcing session \u001b[1;31m(logged out)\u001b[1;0m\n")
            print("\t\t\tPress Any Key to continue...")
            m.getch()
            SignInPage.Logged = False
    def userlogin(self):
        os.system("cls||clear")
        check = "0"
        self.username = input("\t\t\tEnter \u001b[1;31mUsername\u001b[1;0m: ")
        self.userpass = input("\t\t\tEnter \u001b[1;31mPassword\u001b[1;0m: ")
        matchpass = "SELECT password FROM user WHERE name=%s"
        database.execute(matchpass, (self.username,)) #Check's if the password is present in the database! If it's present it loads it!
        check = database.fetchone()
        cred = (('{}').format(self.userpass),)
        if check == cred:
            SignInPage.Logged = True
            SignInPage.user_name = self.username
            SignInPage.user_pass = self.userpass
            print("\t\t\tYou have logged in successfully as\u001b[1;31m", self.username, "\u001b[1;0m")
            time.sleep(1)
        else:
            SignInPage.Logged = False
            print("\t\t\tYou've entered \u001b[1;31mincorrect credentials\u001b[1;0m")
            print("\t\t\tForcing session \u001b[1;31m(logged out)\u001b[1;0m\n")
            print("\t\t\tPress \u001b[1;31mAny\u001b[1;0m Key To Continue...")
            m.getch()