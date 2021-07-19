import os
import mysql.connector
import msvcrt as m
import signinpage as sp
import admin as a
import users as u
from newuser import NewUser as nw

db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="root",
                             database="banking")
database = db.cursor()


# I am gonna learn & implement mySQL on this now! #DONE...
def main():
    end = "y"
    while end == "y":
        Signin = sp.SignInPage()
        Admins = a.Admin()
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
            nw.new_user_createaccount(nw)
        elif Signin.user_choice == "4":
            quit()
    return 0


if __name__ == "__main__":
    main()
