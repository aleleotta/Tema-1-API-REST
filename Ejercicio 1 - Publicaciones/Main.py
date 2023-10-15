from Functions import *

option = 10
print("Welcome!")
while option != 0:
    list()
    option = int(input("Choose an option: "))
    if option == 1:
        showAll()
    if option == 2:
        show(id)
    if option == 3:
        add()
    """if option == 4:
        mofidy()
    if option == 5:
        modify()
    if option == 6:
        delete()"""
    if option == 0:
        print("Have a nice day!")