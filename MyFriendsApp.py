# MyFriendsApp.py – Main program for COMP 170 Final Project
from Friend import Friend
import csv
from datetime import datetime
# ANSI styling functions for terminal output
def bold(text): return f"\033[1m{text}\033[0m"
def green(text): return f"\033[92m{text}\033[0m"
def red(text): return f"\033[91m{text}\033[0m"


friends = []

# Load data from CSV on startup
def load_friends():
    try:
        with open("friends_database.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                friend = Friend(row["first_name"], row["last_name"])
                if row["birth_month"] and row["birth_day"]:
                    friend.set_birthday(int(row["birth_month"]), int(row["birth_day"]))
                friend.email_address = row["email_address"]
                friend.nickname = row["nickname"]
                friend.street_address = row["street_address"]
                friend.city = row["city"]
                friend.state = row["state"]
                friend.zip = row["zip"]
                friend.phone = row["phone"]
                friends.append(friend)
    except FileNotFoundError:
        pass

# Save data to CSV on exit
def save_friends():
    with open("friends_database.csv", "w", newline="") as f:
        fieldnames = ["first_name", "last_name", "birth_month", "birth_day", "email_address",
                      "nickname", "street_address", "city", "state", "zip", "phone"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for fnd in friends:
            writer.writerow({
                "first_name": fnd.first_name,
                "last_name": fnd.last_name,
                "birth_month": fnd._birthday.get_month() if fnd._birthday else '',
                "birth_day": fnd._birthday.get_day() if fnd._birthday else '',
                "email_address": fnd.email_address,
                "nickname": fnd.nickname,
                "street_address": fnd.street_address,
                "city": fnd.city,
                "state": fnd.state,
                "zip": fnd.zip,
                "phone": fnd.phone
            })

# Manually enter friend

def load_custom_csv():
    path = input("Enter path to CSV file: ")
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                friend = Friend(row["first_name"], row["last_name"])
                if row["birth_month"] and row["birth_day"]:
                    friend.set_birthday(int(row["birth_month"]), int(row["birth_day"]))
                friend.email_address = row["email_address"]
                friend.nickname = row["nickname"]
                friend.street_address = row["street_address"]
                friend.city = row["city"]
                friend.state = row["state"]
                friend.zip = row["zip"]
                friend.phone = row["phone"]
                friends.append(friend)
                count += 1
            print(green(f"Loaded {count} friend(s) from file."))
    except Exception as e:
        print(red(f"Failed to load file: {e}"))

def add_friend():
    first = input("First name: ")
    last = input("Last name: ")
    friend = Friend(first, last)
    try:
        month = int(input("Birth month (1–12): "))
        day = int(input("Birth day: "))
        friend.set_birthday(month, day)
    except:
        print("Invalid birthday input — skipped.")
    friend.email_address = input("Email: ")
    friend.nickname = input("Nickname: ")
    friend.street_address = input("Street: ")
    friend.city = input("City: ")
    friend.state = input("State: ")
    friend.zip = input("ZIP: ")
    friend.phone = input("Phone: ")
    friends.append(friend)

# Edit existing friend
def edit_friend(friend):
    print("Leave blank to keep current value.")
    for attr, label in [("email_address", "Email"), ("nickname", "Nickname"), ("street_address", "Street"),
                        ("city", "City"), ("state", "State"), ("zip", "ZIP"), ("phone", "Phone")]:
        current = getattr(friend, attr)
        new_val = input(f"{label} [{current}]: ")
        if new_val:
            setattr(friend, attr, new_val)

    if input("Change birthday? (y/n): ").lower() == 'y':
        try:
            month = int(input("New birth month: "))
            day = int(input("New birth day: "))
            friend.set_birthday(month, day)
        except:
            print("Invalid birthday input — skipped.")

# Search and manage friend
def search_friend():
    name = input("Search by last name: ").lower()
    found = [f for f in friends if f.last_name.lower() == name]
    if not found:
        print("No match found.")
        return
    for i, f in enumerate(found):
        print(f"{i + 1}. {f}")
    choice = int(input("Select friend to edit/delete (0 to cancel): "))
    if choice == 0: return
    selected = found[choice - 1]
    action = input("Enter 'e' to edit or 'd' to delete: ").lower()
    if action == 'e':
        edit_friend(selected)
    elif action == 'd':
        confirm = input("Type DELETE to confirm: ")
        if confirm == "DELETE":
            friends.remove(selected)
            print("Friend deleted.")

# Reports menu
def report_menu():
    while True:
        print("\nReports")
        print("3.1 - Alphabetical list")
        print("3.2 - Upcoming birthdays")
        print("3.3 - Mailing labels")
        print("3.9 - Return")
        opt = input("Choose: ")
        if opt == '3.1':
            for f in sorted(friends, key=lambda x: x.last_name):
                print(f"{f} {f._birthday}")
        elif opt == '3.2':
            for f in sorted(friends, key=lambda x: x._birthday.days_until() if x._birthday else 9999):
                print(f"{f} - {f._birthday} ({f._birthday.days_until()} days left)")
        elif opt == '3.3':
            for f in friends:
                print(f"{f.first_name} {f.last_name}\n{f.street_address}\n{f.city}, {f.state} {f.zip}\n")
        elif opt == '3.9':
            break
        else:
            print("Invalid.")

# Main app loop
def main_menu():
    load_friends()
    while True:
        print(bold("1 - Create new friend record"))
        print(bold("2 - Search for a friend"))
        print(bold("3 - Run reports"))
        print(bold("4 - Exit"))
        choice = input("Enter choice: ")

        if choice == '1':
            print("1.1 - Add friend manually")
            print("1.2 - Load friends from CSV")
            subchoice = input("Choose 1.1 or 1.2: ")
            if subchoice == "1.1":
                add_friend()
            elif subchoice == "1.2":
                load_custom_csv()
            else:
                print(red("Invalid option."))

        elif choice == '2':
            search_friend()

        elif choice == '3':
            report_menu()

        elif choice == '4':
            save_friends()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
