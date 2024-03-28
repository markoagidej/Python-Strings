# Task 1: Input Length Validator

import string

def set_name():
    name_length_error_msg = "ERROR: Name must be 2 or more characters! Try again."

    name_first = input("Type your first name: ")
    if len(name_first) < 2:
        print(name_length_error_msg)
        exit()

    name_last = input("Type your last name: ")
    if len(name_last) < 2:
        print(name_length_error_msg)
        exit()

#set_name()

# Task 2: Password Complexity Checker

def choose_password(password):
    complexity_error_msg = "The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number."
    flags = [
        False, #  0 - Length
        False, #  1 - uppercase
        False, #  2 - lowercase
        False  #  3 - number
    ]

    if flags[0] == False:
        if len(password) < 8:
            print("Password too short! Must be at least 8 characters long")
            print(complexity_error_msg)
            exit()
        else:
            flags[0] = True

    for char in password:
        if flags[1] == False:
            if char in string.ascii_uppercase:
                flags[1] = True
                continue
        
        if flags[2] == False:
            if char in string.ascii_lowercase:
                flags[2] = True
                continue

        if flags[3] == False:
            if char.isnumeric():
                flags[3] = True
                continue

    if flags[0] == True and flags[1] == True and flags[2] == True and flags[3] == True:
        print("Password set!")
    else:
        if flags[1] == False:
            print("Password must contain at least 1 upper-case letter")
        if flags[2] == False:
            print("Password must contain at least 1 lower-case letter")
        if flags[3] == False:
            print("Password must contain at least 1 number")

        print(complexity_error_msg)
        exit()

# choose_password(input("Enter a password: "))

# Task 3: Email Formatter

valid_extenstions = [
    "com",
    "net",
    "org"
]

email = input("Enter a valid email address (example@domain.com): ")

def check_email(email):

    if email.count("@") == 1:
        user_split = email.split("@")
        if user_split[0]:
            if user_split[1]:
                if user_split[1].count(".") == 1 and user_split[0].count(".") == 0:
                    domain_split = user_split[1].split(".")
                    if domain_split[0] and domain_split[1]:
                        if domain_split[1] in valid_extenstions:
                            print("Email set!")
                        else:
                            print("Email addresses must have a valid extension (.com/.net/.org)")
                            exit()
                    else:
                        print("Email addresses must have a domain following \'@\' and preceding the extension")
                        exit()
                else:
                    print("Email addresses must include a single \'.\'")
                    exit()
            else:                
                print("Email addresses must have a domain and extension following \'@\'")
                exit()
        else:
            print("Email addresses must have content preceding \'@\'")
            exit()
    else:
        print("Email addresses must include a single \'@\'")
        exit()

check_email(email)