import db.diaryDatabase as diaryDatabase
import diary, passwordHasher

#Create User Table
diaryDatabase.createUserTable()

print("Hello!")
print("what's your name?")
name = input()
print("Hello " + name + ".")

#check if there's a user
users = diaryDatabase.readUser()
firstTime = False
if len(users) == 0:
    firstTime = True
    print("I'll create an account for you. Please enter a password...")
    password = input()
    hashedPassword = passwordHasher.hashPassword(password)

    diaryDatabase.saveUser(name, hashedPassword)
    print("Account made")
    users = diaryDatabase.readUser()

for user in users:
    
    if name == user[1]:
        if firstTime == False:
            print("Welcome back " + name + ". \n Please enter your password....")
            password = input()
            if passwordHasher.verifyPassword(user[2], password):
                diary.mainMenu()
        diary.mainMenu()
    else:
        print("Goodbye")
