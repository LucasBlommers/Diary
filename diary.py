import db.diaryDatabase as diaryDatabase

def createDiary():
    print("Please enter a title.")
    title = input()
    print("Write your diary entry.")
    body = input()

    diaryDatabase.saveEntry(title, body)

    mainMenu()

def mainMenu():
    print("Main Menu \n1. Create Diary \n2. Read diary's")
    choice = input()
    
    if choice == "1":
        createDiary()
    if choice == "2":
        readDiary()
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

        selectionStr = input()
        selection = int(selectionStr) - 1
    except:
        print("Invalid option.: ")
        readDiary()

    print("Selection: " + str(selection))
    print("EntryCounter: " + str(entryCounter))
    if selection == entryCounter - 1:
        return mainMenu()
    
    entries[selection]
 

