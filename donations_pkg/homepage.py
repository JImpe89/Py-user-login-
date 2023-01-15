def show_homepage():
    print("      === DonateMe Homepage ===       ")
    print("| 1. Login       | 2. Register       |")
    print("--------------------------------------")
    print("| 3. Donate      | 4. Show Donations |")
    print("--------------------------------------")
    print("|            5.  Exit                |")
    print("--------------------------------------")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation_string = username + "donated" + " $" + str(donation_amt)
    print("Thank you for your donation!")
    return (donation_string)


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations:
        print("Currently, There are no donations.")
    else:
        for donate in donations:
            print(donate)
