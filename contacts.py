import json
contacts = []

def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

def save_contacts():
    with open("contacts.json","w")as f:
        json.dump(contacts,f)

def load_contacts():
    try:
        with open("contacts.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def search_contact(search_name):
    results = []
    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            results.append(contact)
    return results

contacts = load_contacts()

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact by name")
    print("4. Quit")
    choice = input("Enter choice: ")
    if (choice == "1"):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter your email: ")
        add_contact(name, phone, email)
        save_contacts()
    elif (choice == "2"):
        print(contacts)
    elif (choice == "3"):
        search_name = input("Enter name to search: ")
        results = search_contact(search_name)
        if len(results) == 0:
            print("No contacts found.")
        else:
            for r in results:
                print(f"{r['name']} - {r['phone']} - {r['email']}")
    elif (choice == "4"):
        break