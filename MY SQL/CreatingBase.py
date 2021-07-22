import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="root",
                             database="banking")

cursor = db.cursor()
query = "CREATE TABLE user (account_iD int PRIMARY KEY AUTO_INCREMENT, created datetime, name VARCHAR(50) NOT NULL, age smallint NOT NULL, password VARCHAR(50) NOT NULL, bankbal int NOT NULL, account_Type VARCHAR(50) NOT NULL)"
cursor.execute(query)
db.commit()
