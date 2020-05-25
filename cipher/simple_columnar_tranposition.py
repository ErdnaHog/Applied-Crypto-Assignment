import math


def encrypt(key, plaintext):
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(plaintext):
            ciphertext[col] += plaintext[position]
            position += key
    return ''.join(ciphertext)


def decrypt(key, ciphertext):
    numOfColumns = math.ceil(len(ciphertext) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(ciphertext)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for character in ciphertext:
        plaintext[col] += character
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
