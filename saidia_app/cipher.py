import hashlib

def encrypt(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def valid(raw, hash_text):
    return encrypt(raw) == hashed_text
