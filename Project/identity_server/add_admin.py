from package import model
import getpass
from package.token_generator import hash_password
"""Creates the admin user."""
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email address: ")
password = getpass.getpass("Enter password: ")
confirm_password = getpass.getpass("Enter password again: ")
if password != confirm_password:
    print("Passwords don't match")
model.conn.execute('''INSERT INTO user(user_first_name, user_last_name, email, password) VALUES(?,?,?,?)''',
                 (first_name,
                  last_name,
                  email,
                  hash_password(password)))
model.conn.commit()
print('Admin Added Successfully!!')
