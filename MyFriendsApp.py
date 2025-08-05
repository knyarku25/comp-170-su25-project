import csv
from Friend import Friend

FILENAME = "friends_database.csv"
friends = []

def load_friends():
    try:
        with open(FILENAME, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                friend = Friend(row['first_name'], row['last_name'])
                if row['birth_month'] and row['birth_day']:
                    friend.set_birthday(int(row['birth_month']), int(row['birth_day']))
                friend.email_address = row['email_address']
                friend.nickname = row['nickname']
                friend.street_address = row['street_address']
                friend.city = row['city']
                friend.state = row['state']
                friend.zip = row['zip']
                friend.phone = row['phone']
                friends.append(friend)
    except FileNotFoundError:
        pass

def save_friends():
    with open(FILENAME, 'w', newline='') as f:
        fieldnames = ['first_name', 'last_name', 'birth_month', 'birth_day',
                      'email_address', 'nickname', 'street_address', 'city', 'state', 'zip', 'phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for fnd in friends:
            writer.writerow({
                'first_name': fnd.first_name,
                'last_name': fnd.last_name,
                'birth_month': fnd._birthday.get_month() if fnd._birthday else '',
                'birth_day': fnd._birthday.get_day() if fnd._birthday else '',
                'email_address': fnd.email_address,
                'nickname': fnd.nickname,
                'street_address': fnd.street_address,
                'city': fnd.city,
                'state': fnd.state,
                'zip': fnd.zip,
                'phone': fnd.phone
            })

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

def search_friend():
    name = input("Search by last name: ").strip().lower()
    matches = [f for f in friends if f.last_name.lower() == name]
    if not matches:
        print("No matches found.")
        return
    for i, f in enumerate(matches):
        print(f"{i+1}: {f}")
    choice = int(input("Select a number to edit/delete: ")) - 1
    selected = matches[choice]

    action = input("Enter 'e' to edit, 'd' to delete: ").lower()
    if action == 'e':
        edit_friend(selected)
    elif action == 'd':
        confirm = input("Type DELETE to confirm: ")
        if confirm == "DELETE":
            friends.remove(selected)
            print("Deleted.")

def edit_friend(friend):
    print("Leave a field blank to keep current value.")
    for attr, label in [
        ('email_address', 'Email'),
        ('nickname', 'Nickname'),
        ('street_address', 'Street'),
        ('city', 'City'),
        ('state', 'State'),
        ('zip', 'ZIP'),
        ('phone', 'Phone')
    ]:
        current = getattr(friend, attr)
        new = input(f"{label} [{current}]: ")
        if new: setattr(friend, attr, new)

    if input("Change birthday? (y/n): ").lower() == 'y':
        try:
            m = int(input("New birth month: "))
            d = int(input("New birth day: "))
            friend.set_birthday(m, d)
        except:
            print("Invalid input — skipped.")

def report_menu():
    while True:
        print("\nReports")
        print("3.1 - Alphabetical list")
        print("3.2 - Upcoming birthdays")
        print("3.3 - Mailing labels")
        print("3.9 - Return")

        option = input("Select: ")
        if option == '3.1':
            for f in sorted(friends, key=lambda x: x.last_name):
                print(f"{f} {f._birthday}")
        elif option == '3.2':
            for f in sorted(friends, key=lambda x: x._birthday.days_until() if x._birthday else 9999):
                print(f"{f} - {f._birthday} ({f._birthday.days_until()} days left)")
        elif option == '3.3':
            for f in friends:
                print(f"{f.first_name} {f.last_name}")
                print(f"{f.street_address}")
                print(f"{f.city}, {f.state} {f.zip}")
                print()
        elif option == '3.9':
            break
        else:
            print("Invalid.")

def main_menu():
    load_friends()
    while True:
        print("\nMain Menu")
        print("1 - Create new friend record")
        print("2 - Search for a friend")
        print("3 - Run reports")
        print("4 - Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_friend()
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
