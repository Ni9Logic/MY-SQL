import mysql.connector
from datetime import datetime

db1 = mysql.connector.connect(host="localhost", user="root", passwd="root", database = "banking")

db = db1.cursor()

def CreateUser():
    Created = datetime.now()
    Name = input("Enter Name for the user: ")
    Age = input("Enter Age for the user: ")
    Password = input("Enter Password for the user: ")
    BankBalance = input("Enter Bank Balance for the user: ")
    AccountType = input("Enter Account Type for the user: ")
    db.execute("INSERT INTO User (created, name, age, password, bankbal, account_Type) VALUES(%s, %s, %s, %s, %s, %s)", (Created, Name, Age, Password, BankBalance, AccountType))
    db1.commit()

CreateUser()