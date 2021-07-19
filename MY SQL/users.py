import os
import msvcrt as m
import mysql.connector
import signinpage as sp
from newuser import NewUser as nw

db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="banking")
database = db.cursor()

class User(sp.SignInPage, nw): #USER CLASS DONE!
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
        database.execute(account_details, (sp.SignInPage.user_name,))
        display_user_Record  = database.fetchall()
        print("\t\t\tHere is the \u001b[1;31mLIST\u001b[1;0m your \u001b[1;31maccount details\u001b[1;0m")
        print("\n\t\t\tAccount ID \u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][0])
        print("\t\t\tCreated \u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][1])
        print("\t\t\tName \u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][2])
        print("\t\t\tPassword \u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][4])
        print("\t\t\tAge \u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][3])
        print("\t\t\tBank Balance\u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][5])
        print("\t\t\tAccount Type\u001b[1;31m-->\u001b[1;0m ", display_user_Record[0][6])
        print("\n\t\t\tPress \u001b[1;31mAny\u001b[1;0m Key to continue...")
        m.getch()        
    def case2_Withdraw_Amount():
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (sp.SignInPage.user_name,))
        get_bankbal_fromdb  = database.fetchone()
        print("\t\t\tYour Current Bank Balance is:\u001b[1;31m", get_bankbal_fromdb[0] ,"\u001b[1;0m rs/-")
        bankbal = get_bankbal_fromdb[0]
        withdraw = 0
        if withdraw <= 0 or withdraw > bankbal:
            while withdraw <= 0 or withdraw > bankbal:
                withdraw = float(input("\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to \u001b[1;31mwithdraw\u001b[1;0m: "))
        new_bankbal = bankbal - withdraw
        update_BankBal = ("UPDATE user SET bankbal = %s WHERE name=%s")
        database.execute(update_BankBal, (new_bankbal, sp.SignInPage.user_name,))
        db.commit()
        print("\t\t\tYour New Balance is:\u001b[1;31m", new_bankbal,"\u001b[1;0m")
        print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
        m.getch()
    def case3_Deposit_amount():
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (sp.SignInPage.user_name,))
        get_bankbal_fromdb  = database.fetchone()
        print("\t\t\tYour Current Bank Balance is:\u001b[1;31m", get_bankbal_fromdb[0] ,"\u001b[1;0m rs/-")
        bankbal = get_bankbal_fromdb[0]
        deposit = 0
        if deposit <= 0:
            while deposit <= 0:
                deposit = float(input("\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to \u001b[1;31mdeposit\u001b[1;0m: "))

        new_bankbal = bankbal + deposit
        update_BankBal = ("UPDATE user SET bankbal = %s WHERE name=%s")
        database.execute(update_BankBal, (new_bankbal, sp.SignInPage.user_name,))
        db.commit()
        print("\t\t\tYour New Balance is:\u001b[1;31m", new_bankbal,"\u001b[1;0m")
        print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
        m.getch()        
    def case4_Transfer_amount():
        # FOR USER 1
        os.system("cls||clear")
        withdraw_query = "SELECT bankbal FROM user WHERE name=%s"
        database.execute(withdraw_query, (sp.SignInPage.user_name,))
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
            database.execute(update_bankbal_user1, (total_bankbbal_user1, sp.SignInPage.user_name,))
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