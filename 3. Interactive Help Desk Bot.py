# Task 1: Command Parser

command_words = [
    "help",
    "issue",
    "contact support"
]

issue_words = [
    "login",
    "performance",
    "error"
]

def help_desk():
    print("What can I help you with today?")
    query = input().lower()

    # The order in this if block determines priority of type of command
    if command_words[2] in query: # "contact support"
        print("I see you want to contact customer support. let me put you in contact with someone.")
    elif command_words[1] in query: # "issue"
        issue_query(query)
    elif command_words[0] in query: # "help"
        print("Here are some common things you can do that might help.")
    else:
        print("I don't recognize whatyou are trying to say. Please try rewording it.")


# Task 2: Issue Categorizer

def issue_query(query):
    # The order in this if block determines priority of type of command
    if issue_words[0] in query: # "login"
        print("Let me email you your login credentials.")
    elif issue_words[1] in query: # "performance"
        print("Try these troubleshooting techniques to address teh performance of your machine...")
    elif issue_words[2] in query: # "error"
        print("I am sorry you are having this error.")
    else:
        print("Please try to be more specific about your issue.")


help_desk()