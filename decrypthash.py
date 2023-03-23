import hashlib

# Prompt the user to enter the password
password = input("Enter the password to hash: ")

# Hash the password using all available hash algorithms in hashlib library
hashes = {}
hashes['MD5'] = hashlib.md5(password.encode()).hexdigest()
hashes['SHA1'] = hashlib.sha1(password.encode()).hexdigest()
hashes['SHA256'] = hashlib.sha256(password.encode()).hexdigest()
hashes['SHA512'] = hashlib.sha512(password.encode()).hexdigest()

# Print the hashes
for algorithm, hashed_password in hashes.items():
    print(f"{algorithm} hash: {hashed_password}")
