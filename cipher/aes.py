from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def get_random_key(keysize):
    return get_random_bytes(keysize)


def encrypt(key, plaintext_utf8, ciphertext_file, mode):
    file_out = open(ciphertext_file, "wb")
    if mode == "CBC":
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        [file_out.write(x) for x in (cipher.iv, ciphertext)]

    elif mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        file_out.write(ciphertext)

    else:
        if mode == "CFB":
            AES_MODE = AES.MODE_CFB
        else:
            AES_MODE = AES.MODE_OFB
        cipher = AES.new(key, AES_MODE)
        ciphertext = cipher.encrypt(plaintext_utf8)
        [file_out.write(x) for x in (cipher.iv, ciphertext)]
    file_out.close()

    return


# AES decrypt using CBC and IV, with default unpadding (PKCS7)
def decrypt(key, ciphertext_file, mode):
    file_in = open(ciphertext_file, "rb")
    if mode == "CBC":
        iv, ciphertext = [file_in.read(x) for x in (16, -1)]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)

    elif mode == "ECB":
        ciphertext = file_in.read()
        cipher = AES.new(key, AES.MODE_ECB)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)

    else:
        if mode == "CFB":
            AES_MODE = AES.MODE_CFB
        else:
            AES_MODE = AES.MODE_OFB
        iv, ciphertext = [file_in.read(x) for x in (16, -1)]
        cipher = AES.new(key, AES_MODE, iv)
        decryptedtext_utf = cipher.decrypt(ciphertext)
    file_in.close()

    return decryptedtext_utf
