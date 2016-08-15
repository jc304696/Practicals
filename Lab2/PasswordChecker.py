import re

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
special = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", special)
    password = input("> ")

    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    result = 0
    if capital_letter(password) and lower_case_check(password) and number_check(password) and 5<int(len(password))<15 :
       return True


def capital_letter(password):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    capital = 0

    for i in password:
        if i in upper_case:
            capital += 1
    if capital > 0:
        return True

def lower_case_check(password):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    letter = 0

    for i in password:
        if i in lower_case:
            letter += 1
    if letter > 0:
        return True

def number_check(password):
    number = 0
    digit = "0123456789"

    for i in password:
        if i in digit:
            number += 1
    if number > 0:
        return True

def symbol_check(password):
    symbol = 0
    special = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"

    for i in password:
        if i in special:
            symbol += 1
    if symbol > 0:
        return True


main()