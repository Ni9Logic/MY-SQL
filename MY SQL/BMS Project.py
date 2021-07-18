import os
import time
import msvcrt as m
import mysql.connector
import signinpage as sp
import newuser as nw
import admin as a
import users as u
from datetime import datetime
from re import I

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

# I am gonna learn & implement mySQL on this now! #DONE...
def main():
    end = "y"
    while end == "y":
        Signin = sp.SignInPage()
        Admins = a.Admin()
        newuser = nw.NewUser()
        created_user = u.User()
        os.system("cls||clear")
        Signin.login()
        if Signin.user_choice == "1":
            Signin.adminlogin()
            if sp.SignInPage.Logged == True:
                Admins.adminmenu()
            else:
                continue
        elif Signin.user_choice == "2":
            Signin.userlogin()
            if sp.SignInPage.Logged == True:
                created_user.usermenu()
            else:
                continue
        elif Signin.user_choice == "3":
            newuser.new_user_createaccount()
        elif Signin.user_choice == "4":
            quit()
    return 0
main()