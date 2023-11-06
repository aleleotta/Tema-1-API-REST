import random

password = "" # Password declaration.
for i in range(30): # Character generation goes up to 30.
    password = password + chr(random.randint(33, 255)) # chr(index) is used to get the character from the ASCII table with the index. The inverted function is ord(char).
print(password)