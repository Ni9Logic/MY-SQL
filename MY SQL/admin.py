import os
import time
import msvcrt as m
import mysql.connector
import signinpage as sp
import newuser as nw

db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="root",
                             database="banking")
database = db.cursor()


class Admin(sp.SignInPage, nw.NewUser):  # ADMIN CLASS DONE!
    username = "0"
    password = "0"
    admin_choice = 0
    signin = sp.SignInPage()

    def adminmenu(self):
        end = "y"
        while end == "y":
            os.system("cls||clear")
            print("\t\t\t\u001b[1;31m1\u001b[1;0m. Delete Account"
                  )  # Allows admin to delete an account
            print("\t\t\t\u001b[1;31m2\u001b[1;0m. Accounts lists"
                  )  # Allows admin to view) all the list
            print("\t\t\t\u001b[1;31m3\u001b[1;0m. Specific Accounts Details"
                  )  # Allows admin to view specific account's detials.
            print("\t\t\t\u001b[1;31m4\u001b[1;0m. Modify an Account"
                  )  # Allows admin to modify an account
            print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
            print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program")  # Exits
            self.admin_choice = str(
                input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
            if self.admin_choice == "0" or self.admin_choice > "6" or len(
                    self.admin_choice) == 0:
                while self.admin_choice == "0" or self.admin_choice > "6" or len(
                        self.admin_choice) == 0:
                    os.system("cls||clear")
                    print("\t\t\t\u001b[1;31m1\u001b[1;0m. Delete Account"
                          )  # Allows admin to delete an account
                    print("\t\t\t\u001b[1;31m2\u001b[1;0m. Accounts lists"
                          )  # Allows admin to view) all the list
                    print(
                        "\t\t\t\u001b[1;31m3\u001b[1;0m. Specific Accounts Details"
                    )  # Allows admin to view specific account's detials.
                    print("\t\t\t\u001b[1;31m4\u001b[1;0m. Modify an Account"
                          )  # Allows admin to modify an account
                    print("\t\t\t\u001b[1;31m5\u001b[1;0m. Logout")  # Logs out
                    print("\t\t\t\u001b[1;31m6\u001b[1;0m. Turn Off Program"
                          )  # Exits
                    self.admin_choice = str(
                        input("\u001b[1;31m\t\t\tEnter <1-6>: \u001b[1;0m: "))
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
        delaccount = input(
            "\t\t\tEnter the \u001b[1;31mdesired account\u001b[1;0m you want to \u001b[1;31mdelete\u001b[1;0m: "
        )
        select_query = "SELECT * FROM user WHERE name=%s"
        database.execute(select_query, (delaccount, ))
        if not database.fetchall():
            print("\t\t\tNo Such User Exists")
            print("\t\t\tPress Any key to continue...")
            m.getch()
        else:
            delete_query = "DELETE FROM user WHERE name=%s"
            database.execute(delete_query, (delaccount, ))
            length = database.fetchall()
            db.commit()  # MOST IMPORTANT

            if len(length) == 0:
                print(
                    "\t\t\tAccount \u001b[1;31mdeleted Successfully\u001b[1;0m\n\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                )
                m.getch()

    def case2_display_all_accounts():
        os.system("cls||clear")
        print(
            "\t\t\tHere's the \u001b[1;31mlist of all\u001b[1;0m the accounts below:"
        )
        display = "SELECT account_ID, name FROM user"
        database.execute(display)
        displayall = database.fetchall()
        database.execute(display)
        if database.fetchall():
            for i in range(len(displayall)):
                print(
                    "\t\t\t", displayall[i][0], " \u001b[1;31m-->\u001b[1;0m ", displayall[i][1])
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()
        else:
            print(
                "\t\t\t\u001b[1;31mNo\u001b[1;0m Such Record \u001b[1;31mFound\u001b[1;0m!"
            )
            print("\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue...")
            m.getch()

    def case3_sepcific_details():
        os.system("cls||clear")
        search = input(
            "\t\t\tEnter the \u001b[1;31mname\u001b[1;0m of the user: ")
        search_query = "SELECT * FROM user WHERE name=%s"
        display = []
        database.execute(search_query, (search, ))
        display = database.fetchall()
        database.execute(search_query, (search, ))
        if database.fetchall():
            print(
                "\t\t\tHere's the \u001b[1;31mdata\u001b[1;0m below for user \u001b[1;31m",
                search, "\u001b[1;0m")
            print(
                "\n\t\t\tAccount ID \u001b[1;31m-->\u001b[1;0m ", display[0][0])
            print("\t\t\tCreated \u001b[1;31m-->\u001b[1;0m ",
                  display[0][1])
            print("\t\t\tName \u001b[1;31m-->\u001b[1;0m ",
                  display[0][2])
            print(
                "\t\t\tPassword \u001b[1;31m-->\u001b[1;0m ", display[0][4])
            print("\t\t\tAge \u001b[1;31m-->\u001b[1;0m ",
                  display[0][3])
            print(
                "\t\t\tBank Balance\u001b[1;31m-->\u001b[1;0m ", display[0][5])
            print(
                "\t\t\tAccount Type\u001b[1;31m-->\u001b[1;0m ", display[0][6])
            print(
                "\n\t\t\tPress \u001b[1;31mAny\u001b[1;0m Key to continue...")
            m.getch()
        else:
            print(
                "\t\t\tUser \u001b[1;31mnot\u001b[1;0m Found\n\t\t\tPress any \u001b[1;31mkey\u001b[1;0m to continue..."
            )
            m.getch()

    def case4_modify_user():
        os.system("cls||clear")
        modify_user = input(
            "\t\t\tEnter the \u001b[1;31mname\u001b[1;0m of the user: ")
        modify_query = "SELECT name FROM user Where name=%s"
        database.execute(modify_query, (modify_user, ))
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
                    print(
                        "\t\t\t3 \u001b[1;31m-->\u001b[1;0m Update Bank Balance"
                    )
                    print(
                        "\t\t\t4 \u001b[1;31m-->\u001b[1;0m Update Account Type"
                    )
                    print(
                        "\t\t\t5 \u001b[1;31m-->\u001b[1;0m Update User's Age")
                    Enter = input("\t\t\tEnter \u001b[1;31m<1-5>\u001b[1;0m: ")
            if Enter == "1":
                os.system("cls||clear")
                new_Name = input(
                    "\t\t\tEnter \u001b[1;31mNew Username\u001b[1;0m for the user: "
                )
                update_Name = ("UPDATE user SET name = %s WHERE name=%s")
                database.execute(update_Name, (
                    new_Name,
                    modify_user,
                ))
                db.commit()
                print(
                    "\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully"
                )
                print(
                    "\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                )
                m.getch()
            elif Enter == "2":
                os.system("cls||clear")
                new_Pass = input(
                    "\t\t\tEnter \u001b[1;31mNew User's Password\u001b[1;0m for the user: "
                )
                update_Pass = ("UPDATE user SET password = %s WHERE name=%s")
                database.execute(update_Pass, (
                    new_Pass,
                    modify_user,
                ))
                db.commit()
                print(
                    "\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully"
                )
                print(
                    "\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                )
                m.getch()
            elif Enter == "3":
                try:
                    os.system("cls||clear")
                    new_BankBal = input(
                        "\t\t\tEnter \u001b[1;31mNew User's Bank Balance\u001b[1;0m for the user: "
                    )
                    update_BankBal = (
                        "UPDATE user SET bankbal = %s WHERE name=%s")
                    database.execute(update_BankBal, (
                        new_BankBal,
                        modify_user,
                    ))
                    db.commit()
                    print(
                        "\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully"
                    )
                    print(
                        "\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                    )
                    m.getch()
                except:
                    print(
                        "\t\t\t\u001b[1;31mYou cannot put a string value inside an integer value\u001b[1;0m")
                    print(
                        "\t\t\t\u001b[1;31mPress Any key to Continue....\u001b[1;0m")
                    m.getch()
                    

            elif Enter == "4":
                os.system("cls||clear")
                new_Acc_Type = input(
                    "\t\t\tEnter \u001b[1;31mNew User's Account Type\u001b[1;0m for the user: "
                )
                update_Acc_Type = (
                    "UPDATE user SET account_Type = %s WHERE name=%s")
                database.execute(update_Acc_Type, (
                    new_Acc_Type,
                    modify_user,
                ))
                db.commit()
                print(
                    "\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully"
                )
                print(
                    "\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                )
                m.getch()
            elif Enter == "5":
                os.system("cls||clear")
                new_Age = input(
                    "\t\t\tEnter \u001b[1;31mNew User's Age\u001b[1;0m for the user: "
                )
                update_Age = ("UPDATE user SET age = %s WHERE name=%s")
                database.execute(update_Age, (
                    new_Age,
                    modify_user,
                ))
                db.commit()
                print(
                    "\t\t\tUsername \u001b[1;31mmodified\u001b[1;0m Successfully"
                )
                print(
                    "\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
                )
                m.getch()
        else:
            print("\t\t\tUser \u001b[1;31mNOT Found\u001b[1;0m\n")
            print("\t\t\tPress \u001b[1;31mANY\u001b[1;0m key to continue\n")
            m.getch()
