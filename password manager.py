
import json


# This part of the code opens the file called "passwords" and replaces the data in it using the function save_data.
DATA_FILE = "passwords.json"

try: 
    with open(DATA_FILE, "r") as file:
        pm = json.load(file)
except FileNotFoundError:
    pm = {}

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(pm, file)


# A function to open the program. This is automatically shown after you run the program 
def open_program():
    print("Welcome to the Password Manager!")
    a = input("Press 1 to add a new password, press 2 to view, press 3 to delete a password, press 4 to edit, and press E to exit.\n")
    if a == "1":
        add_pass()
        save_data()
    elif a == "2":
        view(pm)
        save_data()
    elif a == "3":
        delete(pm)
        save_data()
    elif a == "4":
        edit(pm)
        save_data()
    elif a == "E":
        save_data()
        exit()
    else:
        print("Invalid. Try again.")
        a = input("Press 1 to add a new password, press 2 to view, press 3 to delete a password.\n")

# A function to add a password.  
def add_pass():
    a = input("Press Y to continue. Press E to exit.\n")
    if a == "Y":
        title = input("Type a title for your password: ")
        password = input("Type a new password: ")
        while title.lower() in pm:
            print(f"Error: Password for '{title}' already exists in the password manager.")
            title = input("Please enter a different title: ")
            password = input("Enter the password: ")
        pm[title.lower()] = password
    elif a == "E":
        print("\nGoing back to the menu....\n")

    open_program()
    
# A function to view the password.
def view(dictionary):
    if not dictionary:
        print("\nThere are no existing passwords.\n")
    else:
        print("Existing passwords:\n")
        for title, password in pm.items():
            formatted_title = title.capitalize()
            print(f"Title: {formatted_title}")
            print(f"Password: {password}")
    open_program()

# A function to edit the password.
def edit(dictionary):
    if not dictionary:
        print("\nThere are no existing passwords.\n")
    else:
        a = input("Which password do you want to edit?\n")
        if a.lower() in pm:
            b = input("\nPress T to edit the title, press P to edit the password, and press E to exit.\n")
            if b == "T":
                c = input("Type in the new title: ")
                pm[c.lower()] = pm.pop(a.lower())
            elif b == "P":
                c = input("Type in the new password: ")
                pm.update({a.lower():c})
            elif b == "E":
                print("\nGoing back to the menu...\n")
                open_program()
            open_program()
        else:
            print("Error: Password doesn't exist.")
            open_program()

# A function to delete the password. 
def delete(dictionary):
    a = input("Press Y to continue. Press E to exit.\n")
    if a == "Y":
        t = input("What is the title of the password you want to delete?\n")
        while t.lower() not in pm:
            print(f"Error: Password doesn't exist.")
            open_program()
            break
        del pm[t.lower()]
        open_program()
    else:
        open_program()



open_program()
