MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
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
    if upper_lower_digit(password) and SPECIAL_CHARS_REQUIRED:
        if check_symbol(password):
            return True
        else:
            return False
    elif upper_lower_digit(password):
        return True
    else:
        return False

def upper_lower_digit(password):
    if any(c.isupper() for c in password) and 5 < int(len(password)) < 15:
        if any(c.islower() for c in password) and any(c.isdigit() for c in password):
            return True
        else:
            return False
    else:
        return False

def check_symbol(password):
    symbol = 0
    special = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
    for i in password:
        if i in special:
            symbol += 1
    if symbol > 0:
        return True
    else:
        return False


main()
