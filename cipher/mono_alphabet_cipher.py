global LETTERS

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(key, plaintext):
    ciphertext = ""
    for character in plaintext:
        if character.upper() in LETTERS:
            index = LETTERS.find(character.upper())
            ciphertext += key[index].upper()
        else:
            ciphertext += character
    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""
    for character in ciphertext:
        if character.upper() in key.upper():
            index = key.upper().find(character.upper())
            plaintext += LETTERS[index]
        else:
            plaintext += character
    return plaintext
