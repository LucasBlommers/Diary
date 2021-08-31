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

if len(users) == 0:
    print("I'll create an account for you. Please enter a password...")
    password = input()
    hashedPassword = passwordHasher.hashPassword(password)

    diaryDatabase.saveUser(name, hashedPassword)
    print("Account made")
    users = diaryDatabase.readUser()

for user in users:
    
    if name == user[1]:
        print("Welcome back " + name + ". \n Please enter your password....")
        password = input()
        if passwordHasher.verifyPassword(user[2], password):
            diary.mainMenu()
            
    else:
        print("Goodbye")
