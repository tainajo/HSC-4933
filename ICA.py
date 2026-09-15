
import _json as json
import os

from anonymate.anonymizer import
from cryptography.fernet import Fernet

KEY_FILE = "encryption.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        encryption_key = f.read()
else:
    encryption_key = Fernet(encryption_key)
    with open(KEY_FILE, "wb") as f:
        f.write(encryption_key)


fake = Faker()
anonymizer = Anonymizer (encryption_key=encryption_key)

length = int(input("Enter the desired number of synthetic patient datasets you would like:"))

data = []
for _ in range(length):
    data.append(fake.profile())

print ("Unencrypted Data:")
print(data)

data_str = json.dumps (data, default= str)

secure_data = anonymizer.encyrpt_text(data_str)

def write_to_file_question (question: str) -> bool: lusage
while True:
    write_decision = input("Would you like to write to file? (Y/N): ")
    if write_decision in ('Y', 'yes'):
        return True
    if write_decision in ('N', 'no'):
        return False

    print("Invalid input. Please enter 'y' or 'n'")

if write_bool == True:
    custom_name = input("Enter the desired name of the file: ")

file_name = (f'{custom_name}.json')
with open(file_name, "w") as f:
    json.dump(data, f, indent=4)

print (f"saved file: {file_name}")
else:
print ("data not saved. All data will be lost when application is closed")


