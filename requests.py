import sqlite3


connection = sqlite3.connect("titanik.db")
cursor = connection.cursor()


cursor.execute("SELECT Name,Age  FROM passengers WHERE Pclass = 1 ")
result = cursor.fetchall()

cursor.execute("SELECT PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked FROM passengers WHERE Embarked = 'S' AND Fare > 50")
result2 = cursor.fetchall()

cursor.execute("SELECT PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked FROM passengers WHERE  Age < 31 AND Age > 19 AND Age IS NOT NULL")
result3 = cursor.fetchall()

cursor.execute("SELECT Name,Sex FROM passengers WHERE Pclass = 3 OR Age < 10")
result4 = cursor.fetchall()

a = 22


#connection.commit
connection.close()


