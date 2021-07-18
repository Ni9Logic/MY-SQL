import os
import time
import msvcrt as m
import mysql.connector
from datetime import datetime
from re import I

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

# I am gonna learn & implement mySQL on this now! #DONE...
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
class Admin(SignInPage, NewUser): #ADMIN CLASS DONE!
    username = "0"
    password = "0"
    admin_choice = 0
    signin = SignInPage()

    def adminmenu(self):
        end = "y"
        while end == "y":
            os.system("cls||clear")
            print("\t\t\t\u001b[1;31m1\u001b[1;0m. Delete Account")  # Allows admin to delete an account
            print("\t\t\t\u001b[1;31m2\u001b[1;0m. Accounts lists")  # Allows admin to view) all the list            
            print("\t\t\t\u001b[1;31m3\u001b[1;0m. Specific Accounts Details") # Allows admin to view specific account's detials.    
            print("\t\t\t\u001b[1;31m4\u001b[1;0m. Modify an Account") # Allows admin to modify an account
            print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
            print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program")  # Exits
            self.admin_choice = str(input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
            if self.admin_choice == "0" or self.admin_choice > "6" or len(self.admin_choice) == 0:
                while self.admin_choice == "0" or self.admin_choice > "6" or len(self.admin_choice) == 0:
                    os.system("cls||clear")
                    print("\t\t\t\u001b[1;31m1\u001b[1;0m. Delete Account")  # Allows admin to delete an account
                    print("\t\t\t\u001b[1;31m2\u001b[1;0m. Accounts lists")  # Allows admin to view) all the list            
                    print("\t\t\t\u001b[1;31m3\u001b[1;0m. Specific Accounts Details") # Allows admin to view specific account's detials.    
                    print("\t\t\t\u001b[1;31m4\u001b[1;0m. Modify an Account") # Allows admin to modify an account
                    print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
                    print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program")  # Exits
                    self.admin_choice = str(input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
            if self.admin_choice == "1":
                Admin.case1_delete_account()
                end = "y"
            elif self.admin_choice == "2":
                Admin.case2_display_all_accounts()
                end = "y"
            elif self.admin_choice == "3":
                Admin.case3_sepcific_details()
                end = "y"
            elif self.admin_choice == "4":
                Admin.case4_modify_user()
                end = "y"
            elif self.admin_choice == "5":
                os.system("cls||clear")
                break
            elif self.admin_choice == "6":
                quit()
    def case1_delete_account():
        os.system("cls||clear")
        delaccount = input("\t\t\tEnter the \u001b[1;31mdesired account\u001b[1;0m you want to \u001b[1;31mdelete\u001b[1;0m: ")
        select_query = "SELECT * FROM user WHERE name=%s"
        database.execute(select_query, (delaccount,))
        if not database.fetchall():
            print("\t\t\tNo Such User Exists")
            print("\t\t\tPress Any key to continue...")
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
        display = "SELECT account_ID, name FROM user"
        database.execute(display)
        displayall = database.fetchall()
        database.execute(display)
        if database.fetchall():
            print("\t\t\t", displayall)
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()
        else:
            print("\t\t\t\u001b[1;31mNo\u001b[1;0m Such Record \u001b[1;31mFound\u001b[1;0m!")
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()
    def case3_sepcific_details():
        os.system("cls||clear")
        search = input("\t\t\tEnter the \u001b[1;31mname\u001b[1;0m of the user: ")
        search_query = "SELECT * FROM user WHERE name=%s"
        display = []
        database.execute(search_query, (search,))
        display = database.fetchall()
        database.execute(search_query, (search,))
        if database.fetchall():
            print("\t\t\tHere's the \u001b[1;31mdata\u001b[1;0m below for user \u001b[1;31m", search, "\u001b[1;0m")
            print("\t\t\t", display)
            print("\t\t\tPress \u001b[1;31mAny\u001b[1;0m Key to continue...")
            m.getch()
        else:
            print("\t\t\tUser \u001b[1;31mnot\u001b[1;0m Found\n\t\t\tPress any \u001b[1;31mkey\u001b[1;0m to continue...")
            m.getch()
    def case4_modify_user():
        os.system("cls||clear")
        modify_user = input("\t\t\tEnter the \u001b[1;31mname\u001b[1;0m of the user: ")
        modify_query = "SELECT name FROM user Where name=%s"
        database.execute(modify_query, (modify_user,))
        if database.fetchall():
            print("\t\t\tUser \u001b[1;31maccount found\u001b[1;0m.....")
            time.sleep(1)
            os.system("cls||clear")
            Enter = "0"
            if Enter == "0" or Enter > "5" or len(Enter) == 0:
                while Enter == "0" or Enter > "5" or len(Enter) == 0:
                    os.system("cls||clear")
                    print("\t\t\tWhat operations do you want to perform?")
                    print("\t\t\t1 \u001b[1;31m-->\u001b[1;0m Update Name")
                    print("\t\t\t2 \u001b[1;31m-->\u001b[1;0m Update Password")
                    print("\t\t\t3 \u001b[1;31m-->\u001b[1;0m Update Bank Balance")
                    print("\t\t\t4 \u001b[1;31m-->\u001b[1;0m Update Account Type")
                    print("\t\t\t5 \u001b[1;31m-->\u001b[1;0m Update User's Age")
                    Enter = input("\t\t\tEnter \u001b[1;31m<1-5>\u001b[1;0m: ")
            if Enter == "1":
                os.system("cls||clear")
                new_Name = input("\t\t\tEnter \u001b[1;31mNew Username\u001b[1;0m for the user: ")
                update_Name = ("UPDATE user SET name = %s WHERE name=%s")
                database.execute(update_Name, (new_Name, modify_user,))
                db.commit()                
                print("\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully")
                print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
                m.getch()
            elif Enter == "2":
                os.system("cls||clear")
                new_Pass = input("\t\t\tEnter \u001b[1;31mNew User's Password\u001b[1;0m for the user: ")
                update_Pass = ("UPDATE user SET password = %s WHERE name=%s")
                database.execute(update_Pass, (new_Pass, modify_user,))
                db.commit()                
                print("\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully")
                print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
                m.getch()
            elif Enter == "3":
                os.system("cls||clear")
                new_BankBal = input("\t\t\tEnter \u001b[1;31mNew User's Bank Balance\u001b[1;0m for the user: ")
                update_BankBal = ("UPDATE user SET bankbal = %s WHERE name=%s")
                database.execute(update_BankBal, (new_BankBal, modify_user,))
                db.commit()                
                print("\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully")
                print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
                m.getch()
            elif Enter == "4":
                os.system("cls||clear")
                new_Acc_Type = input("\t\t\tEnter \u001b[1;31mNew User's Account Type\u001b[1;0m for the user: ")
                update_Acc_Type = ("UPDATE user SET account_Type = %s WHERE name=%s")
                database.execute(update_Acc_Type, (new_Acc_Type, modify_user,))
                db.commit()                
                print("\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully")
                print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
                m.getch()
            elif Enter == "5":
                os.system("cls||clear")
                new_Age = input("\t\t\tEnter \u001b[1;31mNew User's Age\u001b[1;0m for the user: ")
                update_Age = ("UPDATE user SET age = %s WHERE name=%s")
                database.execute(update_Age, (new_Age, modify_user,))
                db.commit()                
                print("\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully")
                print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
                m.getch()
        else:
            print("\t\t\tUser \u001b[1;31mNOT Found\u001b[1;0m\n")
            print("\t\t\tPress \u001b[1;31mANY\u001b[1;0m key to continue\n")
            m.getch()
class User(SignInPage, NewUser): #USER CLASS DONE!
    user_choice = "0"

    def usermenu(self):
        end = "y"
        while end == "y":
            os.system("cls||clear")
            print("\t\t\t\u001b[1;31m1\u001b[1;0m. Check Account Details")  # Allows admin to delete an account
            print("\t\t\t\u001b[1;31m2\u001b[1;0m. Withdraw Amount")  # Allows admin to view) all the list            
            print("\t\t\t\u001b[1;31m3\u001b[1;0m. Deposit Amount") # Allows admin to view specific account's detials.    
            print("\t\t\t\u001b[1;31m4\u001b[1;0m. Transfer Amount") # Allows admin to modify an account
            print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
            print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program")  # Exits
            self.user_choice = str(input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
            if self.user_choice == "0" or self.user_choice > "6" or len(self.user_choice) == 0:
                while self.user_choice == "0" or self.user_choice > "6" or len(self.user_choice) == 0:
                    os.system("cls||clear")
                    print("\t\t\t\u001b[1;31m1\u001b[1;0m. Check Account Details")  # Allows admin to delete an account
                    print("\t\t\t\u001b[1;31m2\u001b[1;0m. Withdraw Amount")  # Allows admin to view) all the list            
                    print("\t\t\t\u001b[1;31m3\u001b[1;0m. Deposit Amount") # Allows admin to view specific account's detials.    
                    print("\t\t\t\u001b[1;31m4\u001b[1;0m. Transfer Amount") # Allows admin to modify an account
                    print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
                    print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program")  # Exits
                    self.user_choice = str(input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
            if self.user_choice == "1":
                User.case1_Check_Account_Details()
                end = "y"
            elif self.user_choice == "2":
                User.case2_Withdraw_Amount()
                end = "y"
            elif self.user_choice == "3":
                User.case3_Deposit_amount()
                end = "y"
            elif self.user_choice == "4":
                User.case4_Transfer_amount()
                end = "y"
            elif self.user_choice == "5":
                os.system("cls||clear")
                break
            elif self.user_choice == "6":
                quit()
    def case1_Check_Account_Details():
        os.system("cls||clear")
        account_details = "SELECT * FROM user WHERE name=%s"
        database.execute(account_details, (SignInPage.user_name,))
        display_user_Record  = database.fetchall()
        print("\t\t\tHere is the \u001b[1;31mLIST\u001b[1;0m your \u001b[1;31maccount details\u001b[1;0m")
        print("\n\t\t\t", display_user_Record , "\n")
        print("\t\t\tPress \u001b[1;31mAny\u001b[1;0m Key to continue...")
        m.getch()        
    def case2_Withdraw_Amount():
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (SignInPage.user_name,))
        get_bankbal_fromdb  = database.fetchone()
        print("\t\t\tYour Current Bank Balance is:\u001b[1;31m", get_bankbal_fromdb[0] ,"\u001b[1;0m rs/-")
        bankbal = get_bankbal_fromdb[0]
        withdraw = 0
        if withdraw <= 0 or withdraw > bankbal:
            while withdraw <= 0 or withdraw > bankbal:
                withdraw = float(input("\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to \u001b[1;31mwithdraw\u001b[1;0m: "))
        new_bankbal = bankbal - withdraw
        update_BankBal = ("UPDATE user SET bankbal = %s WHERE name=%s")
        database.execute(update_BankBal, (new_bankbal, SignInPage.user_name,))
        db.commit()
        print("\t\t\tYour New Balance is:\u001b[1;31m", new_bankbal,"\u001b[1;0m")
        print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
        m.getch()
    def case3_Deposit_amount():
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (SignInPage.user_name,))
        get_bankbal_fromdb  = database.fetchone()
        print("\t\t\tYour Current Bank Balance is:\u001b[1;31m", get_bankbal_fromdb[0] ,"\u001b[1;0m rs/-")
        bankbal = get_bankbal_fromdb[0]
        deposit = 0
        if deposit <= 0:
            while deposit <= 0:
                deposit = float(input("\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to \u001b[1;31mdeposit\u001b[1;0m: "))

        new_bankbal = bankbal + deposit
        update_BankBal = ("UPDATE user SET bankbal = %s WHERE name=%s")
        database.execute(update_BankBal, (new_bankbal, SignInPage.user_name,))
        db.commit()
        print("\t\t\tYour New Balance is:\u001b[1;31m", new_bankbal,"\u001b[1;0m")
        print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
        m.getch()        
    def case4_Transfer_amount():
        # FOR USER 1
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (SignInPage.user_name,))
        get_bankbal_fromdb  = database.fetchone()
        print("\t\t\tYour Current Bank Balance is:\u001b[1;31m", get_bankbal_fromdb[0] ,"\u001b[1;0m rs/-")
        bankbal_user1 = get_bankbal_fromdb[0] #TOTAL BALANCE OF USER 1
        transfer_amount = 0
        if transfer_amount <= 0 or transfer_amount > bankbal_user1:
            while transfer_amount <= 0 or transfer_amount > bankbal_user1:
                transfer_amount = float(input("\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m to \u001b[1;31mtransfer\u001b[1;0m: "))
        user2 = input("\t\t\tEnter the \u001b[1;31mother person's\u001b[1;0m name: ")
        search_query = "SELECT name FROM user WHERE name=%s"
        database.execute(search_query, (user2,))
        if database.fetchone():
            print("\t\t\tOperation \u001b[1;31mSuccessfully Performed\u001b[1;0m")
            total_bankbbal_user1 = bankbal_user1 - transfer_amount
            update_bankbal_user1 = "UPDATE user SET bankbal=%s WHERE name=%s"
            database.execute(update_bankbal_user1, (total_bankbbal_user1, SignInPage.user_name,))
            db.commit()
                # WORK FOR USER 1 IS DONE
            search_query = ("SELECT bankbal FROM user WHERE name=%s")
            database.execute(search_query, (user2,))
            get_bankbal_fromdb2  = database.fetchone()
            bankbal_user2 = get_bankbal_fromdb2[0]
            total_bankbbal_user2 = bankbal_user2 + transfer_amount
            update_bankbal_user2 = "UPDATE user SET bankbal=%s WHERE name=%s"
            database.execute(update_bankbal_user2, (total_bankbbal_user2, user2,))
            db.commit()
            print("\t\t\tYour New Balance after transfer_amount is: ", total_bankbbal_user1)
            m.getch()
        else:
            print("\t\t\tNo such user found in database\n")
            m.getch()

def main():
    end = "y"
    while end == "y":
        Signin = SignInPage()
        Admins = Admin()
        newuser = NewUser()
        created_user = User()
        os.system("cls||clear")
        Signin.login()
        if Signin.user_choice == "1":
            Signin.adminlogin()
            if SignInPage.Logged == True:
                Admins.adminmenu()
            else:
                continue
        elif Signin.user_choice == "2":
            Signin.userlogin()
            if SignInPage.Logged == True:
                created_user.usermenu()
            else:
                continue
        elif Signin.user_choice == "3":
            newuser.new_user_createaccount()
        elif Signin.user_choice == "4":
            quit()
    return 0
main()