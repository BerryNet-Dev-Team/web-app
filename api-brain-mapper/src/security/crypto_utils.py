from .bcrypt import bcrypt

def hashPassword(password):
    return bcrypt.generate_password_hash(password, 10).decode('utf-8')

def checkPasswordHash(pw_hash, password):
    return bcrypt.check_password_hash(pw_hash, password)
