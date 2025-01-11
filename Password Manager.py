import json
import os
from cryptography.fernet import Fernet

# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to load the key from a file
def load_key():
    return open("secret.key", "rb").read()

# Function to save the key to a file
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to encrypt a password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to save passwords to a JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

# Function to load passwords from a JSON file
def load_passwords():
    if not os.path.exists("passwords.json"):
        return {}
    with open("passwords.json", "r") as f:
        return json.load(f)

# Function to add a password
def add_password(service, password):
    passwords = load_passwords()
    encrypted_password = encrypt_password(password)
    passwords[service] = encrypted_password.decode()
    save_passwords(passwords)
    print(f"Password for {service} added successfully.")

# Function to retrieve a password
def get_password(service):
    passwords = load_passwords()
    if service in passwords:
        encrypted_password = passwords[service].encode()
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Password for {service}: {decrypted_password}")
    else:
        print(f"No password found for {service}.")

# Function to delete a password
def delete_password(service):
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for {service} deleted successfully.")
    else:
        print(f"No password found for {service}.")

# Main function to run the password manager
def main():
    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add_password(service, password)
        elif choice == '2':
            service = input("Enter the service name: ")
            get_password(service)
        elif choice == '3':
            service = input("Enter the service name: ")
            delete_password(service)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    