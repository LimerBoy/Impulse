# Import modules
from hashlib import md5
from string import ascii_letters


# Get salt numbers
def getSaltByKey(key, message):
    salt = ''
    kHash = md5(key.encode()).hexdigest()

    while True:
        for char in kHash:
            if len(salt) == len(message):
                break
            if not char in ascii_letters:
                salt += char

        if len(salt) == len(message):
            return salt
