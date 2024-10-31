from cryptmoji import encrypt,decrypt
import os

source_file = input("Enter the file that needs to be decrypted: ")
key = input("Enter the key for same key used for encryption: ")


filename, extension = os.path.splitext(source_file)
destination_file = f"{filename}_decrypted{extension}"

with open(source_file,'r') as source:
    content = source.read()

content = decrypt(content,key=key)

with open(destination_file,'w') as destination:
    destination.write(content)
print(f"Decryption completed successfully! Encrypted content saved to {destination_file}")
