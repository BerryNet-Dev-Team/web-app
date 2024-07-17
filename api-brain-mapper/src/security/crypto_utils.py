import hashlib

def hashPassword(password):
    bytes = password.encode('utf-8')
    sha = hashlib.sha256()
    sha.update(bytes)
    return sha.hexdigest()