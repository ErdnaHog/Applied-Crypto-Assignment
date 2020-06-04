# Initializing variables required
# errorMessage = "Error: Length of Key Must be >= Length of Plaintext"
mappingsDict = {}


# def main():

#     print()
#     # Taking inputs from the user
#     plaintext = input("Enter the plaintext : ")
#     key = input("Enter the key (length should be >= length of plaintext) : ")
#     print()

#     # Initializing alphabets for rotating
#     alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
#     # Initializing values to alphabets
#     for alphabet in alphabets:
#         mappingsDict[alphabet] = ord(alphabet) - 65

#     plaintext = plaintext.upper()
#     key = key.upper()

#     # Checking if key is invalid
#     if len(key) < len(plaintext):
#         print(errorMessage)
#     # Else applying algorithm
#     else:
#         # Encryption
#         ciphertext = vernamEncryption(plaintext, key)

#         # Decryption
#         plaintext = vernamDecryption(ciphertext, key)

#         # Printing answers
#         print()
#         print("Encrypted ciphertext is : ", ciphertext)
#         print("Decrypted plaintext is  : ", plaintext)
#         print()
#     return


def encrypt(key, plaintext):
    """Function to encrypt the plaintext using Vernam Encryption."""

    # Initializing alphabets for rotating
    alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
    # Initializing values to alphabets
    for alphabet in alphabets:
        mappingsDict[alphabet] = ord(alphabet) - 65

    # Initializing ciphertext
    ciphertext = ''

    for i in range(len(plaintext)):
        ptLetter = plaintext[i]
        keyLetter = key[i]
        if ptLetter in alphabets:
            # Performing vernam encryption step
            sum = mappingsDict[ptLetter] + mappingsDict[keyLetter]
            # Subtracting 26 if sum overflows above values
            if sum >= 26:
                sum -= 26
            # Adding to ciphertext
            ciphertext += chr(sum + 65)
        else:
            ciphertext += ptLetter

    # Returning ciphertext
    return ciphertext


def decrypt(key, ciphertext):
    """Function to decrypt the ciphertext using Vernam Decryption."""

    # Initializing alphabets for rotating
    alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
    # Initializing values to alphabets
    for alphabet in alphabets:
        mappingsDict[alphabet] = ord(alphabet) - 65

    # Initializing plaintext
    plaintext = ''

    for i in range(len(ciphertext)):
        ctLetter = ciphertext[i]
        keyLetter = key[i]
        if ctLetter in alphabets:
            # Performing vernam decryption step
            diff = mappingsDict[ctLetter] - mappingsDict[keyLetter]
            # Adding 26 if diff underflows above values
            if diff < 0:
                diff += 26
            # Adding to plaintext
            plaintext += chr(diff + 65)
        else:
            plaintext += ctLetter

    # Returning plaintext
    return plaintext
