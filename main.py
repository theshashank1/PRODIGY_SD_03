
from contact import Contact, ContactManager
def main() :
    manager = ContactManager()

    while True :
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1' :
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2' :
            manager.view_contacts()
        elif choice == '3' :
            index = int(input("Enter contact index to edit: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            manager.edit_contact(index, name or None, phone or None, email or None)
        elif choice == '4' :
            index = int(input("Enter contact index to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '5' :
            break
        else :
            print("Invalid choice, please try again.")


if __name__ == "__main__" :
    main()
