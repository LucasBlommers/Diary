import db.diaryDatabase as diaryDatabase

def createDiary():
    print("Please enter a title.")
    title = input()
    print("Write your diary entry.")
    body = input()

    diaryDatabase.saveEntry(title, body)

    mainMenu()

def mainMenu():
    print("Main Menu \n1. Create Entry.\n2. Read Entries \n3. Delete Entrie")
    choice = input()
    
    if choice == "1":
        createDiary()
    if choice == "2":
        readDiary()
    if choice == "3":
        deleteDiary()
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
