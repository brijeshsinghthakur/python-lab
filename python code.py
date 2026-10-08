# Address Book in Python

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Address Book ---")
    for name, details in contacts.items():
        print("Name:", name)
        print("Phone:", details["Phone"])
        print("Email:", details["Email"])
        print("Address:", details["Address"])
        print("--------------------")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\nContact Found!")
        print("Name:", name)
        print("Phone:", contacts[name]["Phone"])
        print("Email:", contacts[name]["Email"])
        print("Address:", contacts[name]["Address"])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        contacts[name]["Phone"] = input("Enter new phone number: ")
        contacts[name]["Email"] = input("Enter new email: ")
        contacts[name]["Address"] = input("Enter new address: ")

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# Main Menu
while True:
    print("\n===== ADDRESS BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()s
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Address Book!")
        break
    else:
        print("Invalid choice! Please try again.")