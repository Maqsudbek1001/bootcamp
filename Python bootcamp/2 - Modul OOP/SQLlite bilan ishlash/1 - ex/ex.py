from sqlite3 import connect

'''db = connect('contacts.db')
books_cursor = db.cursor()
student_cursor = db.cursor()
books_cursor.execute("")
books_cursor.fetchall()'''



# with connect('contacts.db') as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE contacts(
#         firs_name VARCHAR,
#         last_name  VARCHAR,
#         phone_number VARCHAR
#         )
#         """
#     )

# with connect('contacts.db') as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS contacts(
#         firs_name VARCHAR,
#         last_name  VARCHAR,
#         phone_number VARCHAR
#         )
#         """
#     )
#     # cursor.execute(
#     #     """
#     #     INSERT INTO contacts (firs_name, last_name, phone_number)
#     #     VALUES ('Maqsud', 'Maxmudov', '+998919098087')
#     #     """
#     # )s
#     cursor.execute(
#         """
#         SELECT * FROM contacts
#         """
#     )
#     rows = cursor.fetchall()
#     print(rows)
import sys
import sqlite3
from prettytable import PrettyTable

class ContactsRspons:
    def __init__(self, db):
        self.db = db

    def add(self, first_name, last_name, phone_number):
        print("Create Contact")

    def list(self):
        with self.db:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            if rows:
                table = PrettyTable(['First Name', 'Last Name', 'Phone Number'])
                for row in rows:
                    table.add_row(row)
                print(table)
            else:
                print("No contacts found.")

    def search(self, first_name):
        with self.db:
            cursor = self.db.cursor()
            cursor.execute("select * from finance where type='earn'")
            rows = cursor.fetchall()
            if rows:
                table = PrettyTable(['First Name', 'Last Name', 'Phone Number'])
                for row in rows:
                    table.add_row(row)
                print(table)
            else:
                print("No contacts found.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Only 1 argument is required")

    available_commands = ('add', 'list', 'search')
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f"Unknown command: {command} \n Available commands: {', '.join(available_commands)}")

    with sqlite3.connect('contacts.db') as db:
        repo = ContactsRspons(db)
        if command == 'add':
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            phone_number = input('Phone Number: ')
            repo.add(first_name, last_name, phone_number)
            print("Contact Successfully Created")
        elif command == 'list':
            repo.list()
        elif command == 'search':
            first_name = input('First Name: ')
            repo.search(first_name)
