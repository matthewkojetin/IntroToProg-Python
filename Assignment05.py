# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# mkoj,5.18.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt" # A string that represents the filename
objFile = None # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {task,priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """   # A menu of user options
strChoice = "" # A Capture the user option selection
strRemoveChoice = "" # A string used to capture data about which item to remove from the list
boolRemove = False # A boolean value that determines if "No matching item." is displayed in the removal step



# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Try/except error handling if file doesn't exist or doesn't contain data
try:
    objFile = open(strFile, "r")
    for strData in objFile:
        lstRow = strData.split(",")
        dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
    print("Data loaded from file \"ToDoList.txt\"")
except:
    print("No existing data in file \"ToDoList.txt\"")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("----------------------------------------")
        print("Current data:\n")
        print("Task | Priority")
        for dicRow in lstTable:
            print(dicRow["task"], dicRow["priority"], sep=' | ')
        print("----------------------------------------")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("----------------------------------------")
        print("Add task to list:\n")
        dicRow = {"task":str(input("Task: ")).strip(), "priority":str(input("Priority: ")).strip()}  # adds inputs to task and priority key
        lstTable.append(dicRow)  # adds row to table
        print("----------------------------------------")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("----------------------------------------")
        print("Remove an item from the list:\n")
        for dicRow in lstTable:
            print(dicRow["task"])
        print("\n")
        boolRemove = False
        strRemoveChoice = input(str("Enter task would you like to remove: ")).strip()
        for dicRow in lstTable:
            if dicRow["task"].lower() == strRemoveChoice.lower():
                lstTable.remove(dicRow)
                print(strRemoveChoice + " removed.")
                boolRemove = True
        if boolRemove == False:
            print("No matching item.")
        print("----------------------------------------")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("----------------------------------------")
        objFile = open(strFile, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")  # Process the data into the file
            print(dicRow["task"] + "," + dicRow["priority"] + " saved to file.")  # Display a message to the user
        print("----------------------------------------")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
    else:
        # Catch-all in case user enters a value that is not valid
        print("----------------------------------------")
        print("Invalid selection.")
        print("----------------------------------------")\

input("\n\nPress the ENTER key to exit.")
