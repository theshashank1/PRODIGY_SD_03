import json


class Contact :
    def __init__(self, name, phone, email) :
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) :
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

    def to_dict(self) :
        return {
            'name' : self.name,
            'phone' : self.phone,
            'email' : self.email
        }

    @classmethod
    def from_dict(cls, data) :
        return cls(data['name'], data['phone'], data['email'])


class ContactManager :
    def __init__(self, filename='contacts.json') :
        self.contacts = []
        self.filename = filename
        self.load_from_file()

    def add_contact(self, name, phone, email) :
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_to_file()

    def view_contacts(self) :
        for i, contact in enumerate(self.contacts, start=1) :
            print(f"{i}. {contact}")

    def edit_contact(self, index, name=None, phone=None, email=None) :
        if 0 <= index < len(self.contacts) :
            if name :
                self.contacts[index].name = name
            if phone :
                self.contacts[index].phone = phone
            if email :
                self.contacts[index].email = email
            self.save_to_file()
        else :
            print("Invalid contact index.")

    def delete_contact(self, index) :
        if 0 <= index < len(self.contacts) :
            del self.contacts[index]
            self.save_to_file()
        else :
            print("Invalid contact index.")

    def save_to_file(self) :
        with open(self.filename, 'w') as file :
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def load_from_file(self) :
        try :
            with open(self.filename, 'r') as file :
                contacts_data = json.load(file)
                self.contacts = [Contact.from_dict(data) for data in contacts_data]
        except FileNotFoundError :
            self.contacts = []
