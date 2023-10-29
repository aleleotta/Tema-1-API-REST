from Petitions import *

def list():
    print("CRUD List:")
    print("    1) Add")
    print("    2) Show list")
    print("    3) Search")
    print("    4) Update ")
    print("    5) Delete")
    print("    0) Exit")

option = 10
print("Welcome!")
while option != 0:
    list()
    try:
        option = int(input("Introduce an option from above: "))
    except:
        print("The option must be an integer!")
        continue
    if option == 1:
        POST()
    elif option == 2:
        GET()
    elif option == 3:
        GET1()
    elif option == 4:
        option1 = 10
        while option1 != 1 and option1 != 2:
            try:
                option1 = int(print("Would you like to update an entire registry or a specific attribute in a registry? 1) Update all 2) Update specific attribute"))
                if option1 != 1 and option1 != 2:
                    print("Please introduce a valid option!")
            except:
                print("The option must be an integer!")
        if option1 == 1:
            PUT()
        if option1 == 2:
            PATCH()
    elif option == 5:
        DELETE()
    elif option == 0:
        print("Have a great day!")
    else:
        print("Please introduce a valid option!")