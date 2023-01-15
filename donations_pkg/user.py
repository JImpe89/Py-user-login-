
def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("\nWelcome to my donateMe page")
            return username
        else:
            print("Password does not match" + str(""))
    else:
        print("Username not found!")
        return " "


def register(database, username):
    if username in database:
        print("Username already exist")
        return " "
    else:
        print(username, "Has been registered")
        return username
