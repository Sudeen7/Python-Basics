"""
basic contact book that allows insertion, search, deletion.
uses regex for email validation.
"""
import re
# add, view, remove, search

contactBook = {}  # dictionary


def is_emptyBook():
    if not contactBook:
        print("No contacts in the book!")
        return True
    return False


def validatePhone(phoneVal):

    if not phoneVal.isdigit:
        print("Phone number can only consist digits!")
        return False
    if len(phoneVal) != 10:
        print("Phone number must be 10 digits!")
        return False
    return True


def validateEmail(emailVal):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patternValidation = re.match(pattern, emailVal)
    if not patternValidation:
        print("Enter a valid email (example12@gmail.com)!")
        return False
    return True


def addContact():
    name = input("Enter name of the contact to add: ").strip()
    if name in contactBook:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if validatePhone(phone) and validateEmail(email):
        contactBook[name] = {'phone': phone,
                             'email': email}  # inner dictionary
        print("Contact added succesfully!")
    else:
        print("Error adding contact, Try Again!")


def viewContactBook():
    if is_emptyBook():
        return
    for name, info in contactBook.items():
        print(f"Name: {name}")
        print(f"Phone No.: {info['phone']}")
        print(f"Email address: {info['email']}")
        print("-"*20)


def searchContact():
    if is_emptyBook():
        return
    name = input("Enter name of contact to search: ")
    if name in contactBook:
        print("Contact Found!")
        print(f"Name: {name}")
        print(f"Phone No.: {contactBook[name]['phone']}")
        print(f"Email address: {contactBook[name]['email']}")
        print("-"*20)
    else:
        print("Error 404! Contact not found.")
        return


def removeContact():
    is_emptyBook()
    name = input("Enter the name of contact to remove: ")
    if name in contactBook:
        del contactBook[name]
        print("Contact deleted successfully!")
    else:
        print("No contact with such name!")
        return


def main():
    while True:
        print("-----Menu:-----")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View Contact Book")
        print("5. Exit")
        user = input("Enter your choice (1-5): ")
        if user == "1":
            addContact()
        if user == "2":
            removeContact()
        if user == "3":
            searchContact()
        if user == "4":
            viewContactBook()
        if user == "5":
            print("Thank You!")
            break


main()
