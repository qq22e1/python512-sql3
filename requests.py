import sqlite3
import csv


data = []
with open("train.csv") as f:
    result = csv.DictReader(f)
    for lines in result:
        data.append(tuple(lines.values()))

connection = sqlite3.connect("titanik.db")
cursor = connection.cursor()


cursor.execute("SELECT Name,Age  FROM passengers WHERE Pclass = '1' ")
result = cursor.fetchall()

cursor.execute("SELECT PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked FROM passengers WHERE Embarked = 'S' AND Fare > 50")
result2 = cursor.fetchall()

cursor.execute("SELECT PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked FROM passengers WHERE  Age < 30 AND Age > 20 AND Age IS NOT NULL")
result3 = cursor.fetchall()



#connection.commit
connection.close()


