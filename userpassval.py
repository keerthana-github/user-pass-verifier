import random


# define functions to keep code clean
# function: to determine if username is alphanumeric
# input: none
# processing: determines if the string username is alphanumeric
# output: boolean
def alphanumeric_username():
    # if statement classifies first condition, is username alphanumeric
    if username.isalnum():
        # return the value accordingly
        return True
    # if the condition is not satisfied
    else:
        # return False
        return False


# function: to determine if the first or last character has digit
# input: string
# processing: determines if last character and first character are numbers
# output: boolean
def first_last(x):
    # calculate the length of the username
    length = len(x)
    # establish the first letter in the index
    first = x[0]
    # establish the last letter in the index using length
    last = x[length - 1]
    # first condition
    if first.isnumeric() or last.isnumeric():
        # if it's met, return false
        return False
    # second condition
    else:
        # if it's met, return true
        return True


# function: to determine how many uppercase letters there are
# input: string
# processing: determines how many characters are uppercase
# output: number of characters (integer)
def uppercase(x):
    # set an accumulator variable
    characters = 0
    # set up a for loop to cycle through each character in the username
    for l in x:
        # if first condition is met,
        if ord(l) >= 65 and ord(l) <= 90:
            # add to the acculumator variable
            characters += 1
    # return the number of characters
    return characters


# function: to determine how many lowercase letters are there
# input: string
# processing: determines how many characters are lowercase
# output: number of characters (integer)
def lowercase(x):
    # set an accumulator variable
    characters = 0
    # set up a for loop to cycle through each character in the username
    for l in x:
        # if first condition is met,
        if ord(l) >= 97 and ord(l) <= 122:
            # add to the acculumator variable
            characters += 1
    # return the number of characters
    return characters


# function: to determine how many digits are there
# input: string
# processing: determines how many characters are digits
# output: number of characters (integer)
def digits(x):
    # set an accumulator variable
    digits = 0
    # set up a for loop to cycle through each character in the username
    for i in x:
        # if first condition is met,
        if ord(i) >= 48 and ord(i) <= 57:
            # add to the acculumator variable
            digits += 1
    # return the number of characters
    return digits


# function: determine how many special characters
# input: string
# processing: determines how many characters are special
# output: number of characters (integer)
def special_characters(x):
    # set an accumulator variable
    special = 0
    # set up a for loop to cycle through each character in the username
    for l in x:
        # if first condition is met,
        if ord(l) >= 35 and ord(l) <= 38:
            # add to the acculumator variable
            special += 1
    # return the number of characters
    return special


# function: determine if the username is in the password
# input: none
# processing: determines if username is in the password
# output: boolean
def username_password():
    # if username is in the password return true
    if username in password:
        return True
    # else, return false
    else:
        return False


# while loop to ensure that username is valid
while True:
    # series of print statements that include functions to calculate each condition
    username = input("Enter a username: ")
    print("* Length of username: ", len(username))
    print("* All characters are alpha-numeric: ", alphanumeric_username())
    print("* First & last characters are not digits: ", first_last(username))
    print("* # of uppercase characters in the username: ", uppercase(username))
    print("* # of lowercase characters in the username: ", lowercase(username))
    print("* # of digits in the username: ", digits(username))
    # if all conditions are met,
    if len(username) >= 8 and len(username) <= 15 and alphanumeric_username() == True and first_last(
            username) == True and uppercase(username) >= 1 and lowercase(username) >= 1 and digits(username) >= 1:
        # print statement
        print("Username valid!\n")
        # break out of the loop
        break
    # if not,
    else:
        # then print statement and repeat loop
        print("Username is invalid, please try again.\n")

# while loop to ensure that username is valid
while True:
    # series of print statements that include functions to calculate each condition
    password = input("Enter a password: ")
    print("* Length of password: ", len(password))
    print("* Username is part of password:", username_password())
    print("* # of uppercase characters in the username: ", uppercase(password))
    print("* # of lowercase characters in the username: ", lowercase(password))
    print("* # of digits in the username: ", digits(password))
    print("* # of special characters in the password: ", special_characters(password))
    # if all conditions are met,
    if len(password) >= 8 and username_password() == False and uppercase(password) >= 1 and lowercase(
            password) >= 1 and digits(password) >= 1 and special_characters(password) >= 1:
        # print statement
        print("Password is valid!")
        # break out of the loop
        break
    # if not,
    else:
        # then print statement and repeat loop
        print("Password is invalid, please try again.\n")
        user = input("Would you like us to fix your password for you? ")
        if user.lower() == "yes":
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower = "abcdefghijklmnopqrstuvwxyz"
            digit = "0123456789"
            special = "#$%&"
            all_char = "#$%&0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if username_password() == True:
                rand = random.randint(0, (len(password) - 1))
                temp_password = password[:rand] + random.choice(all_char) + password[rand:]
                password = temp_password
                print("* Username is in password - interrupting string to remove it: ", password)
            if uppercase(password)<1:
                rand = random.randint(0, (len(password) - 1))
                temp_password = password[:rand] + random.choice(upper) + password[rand:]
                password = temp_password
                print("* Adding a random uppercase character at a random position: ", password)
            if lowercase(password)<1:
                rand = random.randint(0, (len(password) - 1))
                temp_password = password[:rand] + random.choice(lower) + password[rand:]
                password = temp_password
                print("* Adding a random lowercase character at a random position: ", password)
            if digits(password)<1:
                rand = random.randint(0, (len(password) - 1))
                temp_password = password[:rand] + random.choice(digit) + password[rand:]
                password = temp_password
                print("* Adding a random digit at a random position: ", password)
            if special_characters(password)<1:
                rand = random.randint(0, (len(password) - 1))
                temp_password = password[:rand] + random.choice(special) + password[rand:]
                password = temp_password
                print("* Adding a random special character at a random position: ", password)
            if len(password) < 8:
                while len(password)<8:
                    rand = random.randint(0, (len(password) - 1))
                    temp_password = password[:rand] + random.choice(all_char) + password[rand:]
                    password = temp_password
                print("* Adding random characters at a random position: ", password)
            break
        elif user.lower() == "no":
            print("Thank you for using our program")            
        else:
            print("Invalid input")
