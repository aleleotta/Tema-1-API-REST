from Petitions import *

option = 10
print("Welcome!")
while option != 0:
    list()
    try:
        option = int(input("Introduce an option from above: "))
    except:
        print("The option must be an integer!")
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 0:
        print("Have a great day!")
    else:
        print("Please introduce a valid option!")

def list():
    print("CRUD List:")
    print("    1) Add")
    print("    2) Show list")
    print("    3) Search")
    print("    4) Update ")
    print("    5) Delete")
    print("    0) Exit")