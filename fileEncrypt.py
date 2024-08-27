from cryptography.fernet import Fernet

# Generate a random encryption key
encryption_key = Fernet.generate_key()

# Create the Fernet cipher using the encryption key
with open('encryptlog.key','wb') as file:
    file.write(encryption_key)
