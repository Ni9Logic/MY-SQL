import os
import time
import msvcrt as m
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

# I am gonna learn & implement mySQL on this now!


class SignInPage:
    userchoice = 1
    admin_name = "0"
    admin_pass = "0"
    Logged = False

    def login(self):
        os.system("cls||clear")
        print(
            "\t\t\tWelcome to \u001b[1;31mSUNUDSS KA BANK! HAHAHA MERA BANK\u001b[1;0m"
        )
        print("\t\t\t1 \u001b[1;31m-->\u001b[1;0m Sign in as admin")
        print("\t\t\t2 \u001b[1;31m-->\u001b[1;0m Sign in as user")
        print("\t\t\t3 \u001b[1;31m-->\u001b[1;0m Create a New Account")
        print("\t\t\t4 \u001b[1;31m-->\u001b[1;0m Exit")
        self.user_choice = int(input("\t\t\tEnter: "))
        if self.user_choice == 0 or self.user_choice > 4:
            while self.user_choice == 0 or self.user_choice > 4:
                os.system("cls||clear")
                print("\t\t\tYou've Entered Incorrect Statement.")
                self.user_choice = input("\t\t\tEnter Again: ")
                self.user_choice = int(self.user_choice)
        return self.user_choice

    def adminlogin(self):
        os.system("cls||clear")
        self.admin_name = input("\t\t\tEnter \u001b[1;31mUsername\u001b[1;0m: ")
        self.admin_pass = input("\t\t\tEnter \u001b[1;31mPassword\u001b[1;0m: ")
        if self.admin_name == "admin" and self.admin_pass == "admin":
            os.system("cls||clear")
            print("\n\t\t\tYou've Successfully \u001b[1;31mlogged\u001b[1;0m in as an a\u001b[1;31mdministrator\u001b[1;0m...")
            time.sleep(1)
            SignInPage.Logged = True
        else:
            os.system("cls||clear")
            print(
                "\t\t\t\u001b[1;31mNOTE:\u001b[1;0m You've entered incorrect \u001b[1;31mCredentials\u001b[1;0m"
            )
            print("\t\t\tForcing session \u001b[1;31m(logged out)\u001b[1;0m\n")
            print("\t\t\tPress Any Key to continue...")
            m.getch()
            SignInPage.Logged = False


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
            self.new_user_name = input("\t\t\tEnter\u001b[1;31m Username\u001b[1;0m: ")
            database.execute(select_query, (self.new_user_name,))
            if database.fetchall():
                print("\t\t\tUser Alreasdy Exists")
                print("\t\t\tPress Any key to continue...")
                m.getch()
            else:
                self.created = datetime.now()
                self.new_user_age = input("\t\t\tEnter\u001b[1;31m Age\u001b[1;0m of the user: ")
                self.new_user_pass = input("\t\t\tEnter\u001b[1;31m Password\u001b[1;0m For User: ")
                self.new_user_BankBal = input("\t\t\tEnter\u001b[1;31m Initial_Deposit\u001b[1;0m For User: ")
                print("\t\t\tThere are \u001b[1;31mTwo Types\u001b[1;0m of Banking Accounts\n\t\t\t1 \u001b[1;31m-->\u001b[1;0m Savings \n\t\t\t2 \u001b[1;31m-->\u001b[1;0m Current")
                self.new_user_Account_Type = input("\t\t\tEnter\u001b[1;31m Account_Type\u001b[1;0m For User: ")
                print("\t\t\tAccount \u001b[1;31mSuccessfully Created\u001b[1;0m\n\t\t\tPress Any Key to continue")
                m.getch()
                # Uploading into database
                database.execute("INSERT INTO User (created, name, age, password, bankbal, account_Type) VALUES(%s, %s, %s, %s, %s, %s)", (self.created, self.new_user_name, self.new_user_age, self.new_user_pass, self.new_user_BankBal, self.new_user_Account_Type))
                db.commit()


class Admin(SignInPage, NewUser):
    username = "0"
    password = "0"
    admin_choice = 0
    admin_log = True
    signin = SignInPage()

    def adminmenu(self):
        end = "y"
        while end == "y":
            os.system("cls||clear")
            print("\t\t\t1. Delete Account")  # Allows admin to delete an account
            # Allows admin to view) all the list
            print("\t\t\t2. Accounts lists")
            # Allows admin to view specific account's detials.
            print("\t\t\t3. Specific Accounts Details")
            # Allows admin to modify an account
            print("\t\t\t4. Modify an Account")
            print("\t\t\t5. Logout")  # Logs out
            print("\t\t\t6. Turn Off Program")  # Exits
            self.admin_choice = int(
                input("\u001b[1;31m\t\t\tEnter <1-7>: \u001b[1;0m: ")
            )
            if self.admin_choice == 0 or self.admin_choice > 7:
                while self.admin_choice == 0 or self.admin_choice > 7:
                    os.system("cls||clear")
                    self.admin_choice = int(
                        input("\u001b[1;31m\t\t\tEnter <1-7>: \u001b[1;0m: ")
                    )
            if self.admin_choice == 1:
                Admin.case1_delete_account()
                end = "y"
            elif self.admin_choice == 2:
                Admin.case2_display_all_accounts()
                end = "y"
            elif self.admin_choice == 3:
                Admin.case3_sepcific_details()
                end = "y"
            elif self.admin_choice == 4:
                Admin.case4_modify_user()
                end = "y"
            elif self.admin_choice == 5:
                os.system("cls||clear")
                break
            elif self.admin_choice == 6:
                quit()

    def case1_delete_account():
        os.system("cls||clear")
        delaccount = input("\t\t\tEnter the \u001b[1;31mdesired account\u001b[1;0m you want to \u001b[1;31mdelete\u001b[1;0m: ")
        select_query = "SELECT * FROM user WHERE name=%s"
        database.execute(select_query, (delaccount,))
        if not database.fetchall():
            print("\t\t\tNo \u001b[1;31mSuch\u001b[1;0m User \u001b[1;31mExists\u001b[1;0m")
            print("\t\t\tPress Any \u001b[1;31mkey\u001b[1;0m to continue...")
            m.getch()
        else:
            delete_query = "DELETE FROM user WHERE name=%s"
            database.execute(delete_query, (delaccount,))
            length = database.fetchall()
            db.commit() #MOST IMPORTANT
            if len(length) == 0:
                print("\t\t\tAccount \u001b[1;31mdeleted Successfully\u001b[1;0m\n\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..." )
                m.getch()    

    def case2_display_all_accounts():
        os.system("cls||clear")
        print("\t\t\tHere's the \u001b[1;31mlist of all\u001b[1;0m the accounts below:")
        display = "SELECT name FROM user"
        database.execute(display)
        displayall = database.fetchall()
        if database.fetchall():
            print("\t\t\t", displayall)
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()
        else:
            print("\t\t\t\u001b[1;31mNo\u001b[1;0m Such User \u001b[1;31mFound\u001b[1;0m!")
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()

    def case3_sepcific_details():
        os.system("cls||clear")
        index = 0
        passed = False
        search = input("\t\t\tEnter the \u001b[1;31mname\u001b[1;0m of the user: ")
        with open("usernames.txt", "r") as file:
            for lines in file:
                index = index + 1
                if lines.strip() == search:
                    passed = True
                else:
                    passed = False
        if passed:
            print("\t\t\tUser Found....")
            time.sleep(1)
            print("\t\t\t\u001b[1;31mName\u001b[1;0m of the user is: ", lines)
            with open("passwords.txt", "r") as file:
                print(
                    "\t\t\t\u001b[1;31mPassword\u001b[1;0m of the user is: ",
                    file.readlines(index),
                )
            with open("Account_Type.txt", "r") as file:
                print(
                    "\t\t\t\u001b[1;31mAccount Type\u001b[1;0m of the user is: ",
                    file.readlines(index),
                )
            with open("BankBal.txt", "r") as file:
                print(
                    "\t\t\t\u001b[1;31mBank Balance\u001b[1;0m of the user is: ",
                    file.readlines(index),
                )
            with open("Account_ID.txt", "r") as file:
                print(
                    "\t\t\t\u001b[1;31mAccount ID\u001b[1;0m of the user is: ",
                    file.readlines(index),
                )
            print("\t\t\tPress any key to continue...")
            m.getch()
        else:
            print(
                "\t\t\tUser \u001b[1;31mnot\u001b[1;0m Found\n\t\t\tPress any \u001b[1;31mkey\u001b[1;0m to continue..."
            )
            m.getch()

    def case4_modify_user():
        os.system("cls||clear")
        modify_user_found = False
        modify_user = input("\t\t\tEnter the name of the user: ")
        with open("usernames.txt", "r") as file:
            for line in file:
                if line.strip() == modify_user:
                    modify_user_found = True
        if modify_user_found:
            print("\t\t\tUser account found.....")
            time.sleep(1)
            os.system("cls||clear")
            Enter = "0"
            if Enter == "0" or Enter > "5":
                while Enter == "0" or Enter > "5":
                    os.system("cls||clear")
                    print("\t\t\tWhat operations do you want to perform?")
                    print("\t\t\t1 --> Update Name")
                    print("\t\t\t2 --> Update Password")
                    print("\t\t\t3 --> Update Bank Balance")
                    print("\t\t\t4 --> Update Account Type")
                    print("\t\t\t5 --> Update Account ID")
                    Enter = input("\t\t\tEnter <1-5>: ")
            if Enter == "1":
                os.system("cls||clear")
                Admin.new_usernames = []
                new_name_user = input("\t\t\tEnter New Name of the User: ")
                # I need to test this LOGIC in my code...
                with open("usernames.txt", "r") as file:
                    Admin.usernames = []
                    for line in file:
                        Admin.usernames.append(line)
                print("All usernames are: ", Admin.usernames)
                with open("usernames.txt", "w+") as file:
                    for line in file:
                        print("I get in in for loop")
                        if line.strip() == modify_user:
                            Admin.new_usernames = Admin.usernames.pop(modify_user)
                            Admin.new_usernames.append(new_name_user)
                            print("All new usernames are: ", Admin.new_usernames)
                            file.write(Admin.new_usernames)
                    m.getch()

                    """
                    list = all usernames present in file
                    for i in range list:
                        search in list = input
                        if serachinlist == list[i]
                            list[i].pop(serachinlist)
                        newlist = list
                        newlist = newlist.split()
                    with open("usernames.txt", "w") as file_write:
                        file_write(newlist)
                    """

                    # Commented This LOGIC fails
                    """
                    print("\t\t\tYour old username is:", file.readlines(Admin.index))
                    old_user = file.readlines(Admin.index)
                    old_user = str(old_user)
                    new_user = input("\t\t\tYour new username is: ")
                    file_read = open("usernames.txt", "r")
                    file_write = open("usernames.txt", "a")
                    new_user = str(new_user)
                    for line in file_read:
                    file_write.write(line.replace(old_user, new_user))
                    file_read.close()
                    file_write.close()
                    """
        else:
            print("\t\t\tUser NOT found\n\t\t\tTry Again Later!\n")
            print("\t\t\tPress ANY key to continue\n")
            m.getch()


def main():
    end = "y"
    while end == "y":
        Signin = SignInPage()
        Admins = Admin()
        newuser = NewUser()
        os.system("cls||clear")
        Signin.login()
        if Signin.user_choice == 1:
            Signin.adminlogin()
            if SignInPage.Logged == True:
                Admins.adminmenu()
                if Admins.admin_log == False:
                    continue
            else:
                continue
        elif Signin.user_choice == 3:
            newuser.new_user_createaccount()
        elif Signin.user_choice == 4:
            quit()
    return 0


main()
