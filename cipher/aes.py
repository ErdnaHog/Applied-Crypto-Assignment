from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def get_random_key(keysize):
    return get_random_bytes(keysize)

# AES encrypt using CBC and IV, with default padding (PKCS7)
def encrypt(key, plaintext_utf8, ciphertext_file, mode):
    if mode == "CBC":
        cipher = AES.new(key, AES.MODE_CBC) #Q6
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        # write iv and ciphertext to file
        file_out = open(ciphertext_file, "wb")
        [file_out.write(x) for x in (cipher.iv, ciphertext)]
        file_out.close()

    elif mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))        
        file_out = open(ciphertext_file, "wb")
        file_out.write(ciphertext)
        file_out.close()
        
    else:
        if mode == "CFB":
            AES_MODE = AES.MODE_CFB
        else:
            AES_MODE = AES.MODE_OFB
        cipher = AES.new(key, AES_MODE)
        ciphertext = cipher.encrypt(plaintext_utf8)
        file_out = open(ciphertext_file, "wb")
        [file_out.write(x) for x in (cipher.iv, ciphertext)]
        file_out.close()
        
    return


# AES decrypt using CBC and IV, with default unpadding (PKCS7)
def decrypt(key, ciphertext_file, mode):
    file_in = open(ciphertext_file, "rb")
    if mode =="CBC":
        iv, ciphertext = [file_in.read(x) for x in (16, -1)]
        file_in.close()
        cipher = AES.new(key,AES.MODE_CBC,iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext),AES.block_size)

    elif mode == "ECB":        
        ciphertext = file_in.read()
        file_in.close()
        cipher = AES.new(key,AES.MODE_ECB)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext),AES.block_size)

    else:
        if mode == "CFB":
            AES_MODE = AES.MODE_CFB
        else:
            AES_MODE = AES.MODE_OFB
        iv, ciphertext = [file_in.read(x) for x in (16, -1)]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        decryptedtext_utf = cipher.decrypt(ciphertext)
        
    return decryptedtext_utf
