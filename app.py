from donations_pkg import homepage
from donations_pkg import user
database = {"admin": "password123", "jaycee": "pass321"}
donations = ("donation_string")
authorized_user = " "


homepage.show_homepage()

if authorized_user == " ":
    print("You must be logged in to donate.")
else:
    print("Logged in as: ", authorized_user)


option = (input("Choose an options: "))
if option == "1":
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    authorized_user = user.login(database, username, password)
elif option == "2":
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    authorized_user = user.register(database, username)
    if authorized_user:
        database.update({username: password})
elif option == "3":
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    authorized_user = user.login(database, username, password)
    if authorized_user:
        donation_string = homepage.donate(authorized_user)
elif option == "4":
    homepage.show_donations(donations)
elif option == "5":
    print("\nLeaving DonateMe...")
