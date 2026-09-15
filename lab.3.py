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


