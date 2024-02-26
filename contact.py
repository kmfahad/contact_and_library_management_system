import re

class Contact:
    def __init__(self, name, email, phone_number):
        self.set_name(name)
        self.set_email(email)
        self.set_phone_number(phone_number)

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        self.email = email

    def set_phone_number(self, phone_number):
        if not re.match(r"\d{10}", phone_number):
            raise ValueError("Invalid phone number format")
        self.phone_number = phone_number

def read_contacts_from_file(file_path):
    contacts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contact = Contact(data[0], data[1], data[2])
                contacts.append(contact)
    except FileNotFoundError:
        pass 
    return contacts

def write_contacts_to_file(file_path, contacts):
    with open(file_path, 'w') as file:
        for contact in contacts:
            file.write(f"{contact.name},{contact.email},{contact.phone_number}\n")

def add_contact(contacts, contact):
    contacts.append(contact)

def list_contacts(contacts):
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone_number}")

def search_contact(contacts, search_term):
    results = [contact for contact in contacts if search_term.lower() in contact.name.lower()]
    return results

def delete_contact(contacts, index):
    del contacts[index]

if __name__ == "__main__":
    file_path = "contacts.txt"
    contacts = read_contacts_from_file(file_path)

    while True:
        print("\nContact Management System")
        print("1. Add a contact")
        print("2. List all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                new_contact = Contact(name, email, phone_number)
                add_contact(contacts, new_contact)
                write_contacts_to_file(file_path, contacts)
                print("Contact added successfully!")
            elif choice == "2":
                list_contacts(contacts)
            elif choice == "3":
                search_term = input("Enter search term: ")
                search_results = search_contact(contacts, search_term)
                if search_results:
                    list_contacts(search_results)
                else:
                    print("No matching contacts found.")
            elif choice == "4":
                list_contacts(contacts)
                index_to_delete = int(input("Enter the index of the contact to delete: ")) - 1
                if 0 <= index_to_delete < len(contacts):
                    delete_contact(contacts, index_to_delete)
                    write_contacts_to_file(file_path, contacts)
                    print("Contact deleted successfully!")
                else:
                    print("Invalid index.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
