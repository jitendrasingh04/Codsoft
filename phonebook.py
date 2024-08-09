class Contact:
    def __init__(self, name, phone_number, email="", address=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = [] 

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nName\t\t\tPhone Number\t\tEmail\t\t\tAddress")
        for contact in self.contacts:
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(contact.name, contact.phone_number, contact.email, contact.address))

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print("Name: {}, Phone Number: {}, Email: {}, Address: {}".format(contact.name, contact.phone_number, contact.email, contact.address))
                return
        print("No records found for '{}'.".format(search_term))

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact with name '{}' not found.".format(old_name))

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact with name '{}' not found.".format(name))

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email (optional): ")
            address = input("Address (optional): ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
        elif choice == "5":
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name_to_delete)
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()