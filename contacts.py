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

def delete_contact(delete_name):
    global contacts
    original_length = len(contacts)
    contacts = [c for c in contacts if delete_name.lower() not in c["name"].lower()]
    if len(contacts) < original_length:
        save_contacts()
        print(f"Contact '{delete_name}' deleted.")
    else:
        print(f"No contact found with name '{delete_name}'.")

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
    print("2. Delete contact")
    print("3. View all contacts")
    print("4. Search contact by name")
    print("5. Quit")
    choice = input("Enter choice: ")

    if (choice == "1"):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter your email: ")
        add_contact(name, phone, email)
        save_contacts()

    elif(choice == "2"):
        delete_name = input("Enter name of contact to delete: ")
        delete_contact(delete_name)
        
    elif (choice == "3"):
        print(contacts)
    
    elif (choice == "4"):
        search_name = input("Enter name to search: ")
        results = search_contact(search_name)
        if len(results) == 0:
            print("No contacts found.")
        else:
            for r in results:
                print(f"{r['name']} - {r['phone']} - {r['email']}")
    
    elif (choice == "5"):
        break