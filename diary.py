import db.diaryDatabase as diaryDatabase
import passwordHasher

def initialize():
    #Create User Table
    diaryDatabase.createUserTable()

def loginAndBegin():
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
                    mainMenu()
            mainMenu()
        else:
            print("Goodbye")


def createDiary():
    print("Please enter a title.")
    title = input()
    print("Write your diary entry.")
    body = input()

    diaryDatabase.saveEntry(title, body)

    mainMenu()

def mainMenu():
    print("Main Menu \n1. Create Entry.\n2. Read Entries \n3. Delete Entrie \n4. Exit")
    choice = input()
    
    if choice == "1":
        createDiary()
    if choice == "2":
        readDiary()
    if choice == "3":
        deleteDiary()
    if choice == "4":
        exit()
    else:
        pass

def readDiary():
    #Read the entries from the database
    entries = diaryDatabase.readEntries()
    #Prepare a entry coubter and a selection variable
    entryCounter = 1
    selection = 0

    #For each entry make a menu item
    for entry in entries:
        print(str(entryCounter) + ". " + entry[1])
        entryCounter += 1
    try:
        #Create a back menu button
        print(str(entryCounter) + ". Back")

        selection = int(input()) - 1
    except:
        print("Invalid option.: ")
        readDiary()

    if selection == entryCounter - 1:
        return mainMenu()
    
    #View the selected entry
    selectedEntry = entries[selection]
    print(selectedEntry[1] + "\n" + selectedEntry[2])
    readDiary()
 

def deleteDiary():
    #Read the entries from the database
    entries = diaryDatabase.readEntries()
    #Prepare a entry coubter and a selection variable
    entryCounter = 1
    selection = 0

    #For each entry make a menu item
    for entry in entries:
        print(str(entryCounter) + ". " + entry[1])
        entryCounter += 1
    try:
        #Create a back menu button
        print(str(entryCounter) + ". Back")

        selection = int(input()) - 1
    except:
        print("Invalid option.: ")
        readDiary()

    if selection == entryCounter - 1:
        return mainMenu()
    #Delete the selected entry
    selectedEntry = entries[selection]
    id = selectedEntry[0]
    diaryDatabase.deleteEntry(id)
    mainMenu()
