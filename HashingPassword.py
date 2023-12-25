import bcrypt
import hashlib

def hashingPassword(password: str) -> str:
    new_password = hashlib.sha256(password.encode()).hexdigest()
    return new_password

#print(hashingPassword("1234"))