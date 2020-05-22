global LETTERS

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(key, plaintext):
    ciphertext = ""

    for character in plaintext:
        if character.upper() in LETTERS:
            position = LETTERS.find(character.upper())
            position = position + key
            if position >= len(LETTERS):
                position = position - len(LETTERS)
            ciphertext += LETTERS[position]
        else:
            ciphertext += character

    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""

    for character in ciphertext:
        if character.upper() in LETTERS:
            position = LETTERS.find(character.upper())
            position -= key
            if position < 0:
                position += len(LETTERS)
            plaintext += LETTERS[position]
        else:
            plaintext += character

    return plaintext
