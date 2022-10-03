ToDoList = []


def addNewItems():
    global ToDoList
    global c
    dtobj1 = 0
    datetime_obj = 0
    TaskCreator = (input("Please input a task "))
    CheckItemsExist(TaskCreator)
    while dtobj1 <= datetime_obj:
        from datetime import datetime
        dt_str = input("Please enter a task date")
        dtobj1 = datetime.strptime(dt_str, "%d/%m/%Y %H:%M:%S")

        import datetime
        datetime_obj = datetime.datetime.now()
        if (dtobj1 <= datetime_obj):
            print('Time entered is in the past! Select the options again')
        else:
            X = ("", "", TaskCreator, dtobj1)
            ToDoList.append(X)
            ToDoList.sort(reverse=False, key=takeSecond)


def printListItems():
    global ToDoList
    for i, elem in enumerate(ToDoList, 0):
        print("{0}. {1} - {2}".format(i, elem[2], elem[3]))
    return


def removelistitems():
    global ToDoList
    deletechoice = int(input("please chose a item to delete"))
    if ToDoList[deletechoice] in ToDoList:
        del ToDoList[deletechoice]
        print('task was deleted')
    else:
        print('that item is not available,please try again!')


def CheckItemsExist(taskName):
    global ToDoList
    for i in ToDoList:
        if taskName == i[0]:
            return True
        else:
            return False


def takeSecond(element):
    return element[2]


def MainMenu():
    print("welcome To Task Manager!")
    print("1.Enter a new To do item ")
    print("2.Print the list of all To do items")
    print("3.Remove a To do item")
    print("4.exit the program")


while True:
    MainMenu()
    choice = int(input('please chose an option'))

    if (choice == 1):
        addNewItems()

    if (choice == 2):
        printListItems()

    if (choice == 3):
        removelistitems()

    if (choice == 4):
        print("you have exited the program")
        break;
