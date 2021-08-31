import db.diaryDatabase as diaryDatabase

def createDiary():
    print("Please enter a title.")
    title = input()
    print("Write your diary entry.")
    body = input()

    diaryDatabase.saveEntry(title, body)

    mainMenu()

def mainMenu():
    print("Main Menu \n1. Create Diary \n2. List of diary's")
    choice = input()
    
    if choice == "1":
        createDiary()
    else:
        pass

def readDiary():
    pass