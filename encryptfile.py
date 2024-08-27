# Read key from file   
key=''
with open('encryptlog.key','rb') as file:
    key=file.read()

# Read data from file
data=''
with open('keylog.txt','rb') as file:
    data = file.read()

#Encrypt the data
from cryptography.fernet import Fernet
f= Fernet(key)

encryptedData=f.encrypt(data)

with open('Encryptlog.txt','wb') as file:
    file.write(encryptedData)