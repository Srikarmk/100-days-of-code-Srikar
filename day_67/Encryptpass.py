import bcrypt
password="Saisrikar1"
salt=bcrypt.gensalt()
passwordHashed=bcrypt.hashpw(bytes(password),salt)
print(passwordHashed)

#How to encrypt password for privacy protection in python 