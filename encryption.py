from cryptmoji import encrypt
import os

source_file = input("Enter the file that needs to be encrypted: ")
key = input("Enter the key for encryption: ")


filename, extension = os.path.splitext(source_file)
destination_file = f"{filename}_encrypted{extension}"

with open(source_file,'r') as source:
    content = source.read()

content = encrypt(content,key=key)

with open(destination_file,'w') as destination:
    destination.write(content)
print(f"Encryption completed successfully! Encrypted content saved to {destination_file}")
