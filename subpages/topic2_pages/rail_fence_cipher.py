from main import mainframe
from tkinter import Label, Text, Button, Message, Frame, Entry
from subpages import clear_screen
from cipher.rail_fence_cipher import encrypt, decrypt

class Rail_fence_cipher:
    def rail_fence_cipher_page():
        clear_screen(mainframe)
    # ? Title
        Label(mainframe, text="Rail Fence Cipher").grid(
            row=0, column=0, columnspan=3)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe)
        plaintext_frame.grid(row=1, column=0)
        plaintext = Label(plaintext_frame, text="Plaintext:")
        plaintext.grid(row=0, column=0, padx=10, pady=10)
        plaintext_input = Text(plaintext_frame, width=20, height=10)
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe)
        ciphertext_frame.grid(row=1, column=2)
        ciphertext = Label(ciphertext_frame, text="Ciphertext:")
        ciphertext.grid(row=0, column=0, padx=10, pady=10)
        ciphertext_input = Text(ciphertext_frame, width=20, height=10)
        ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe)
        key_frame.grid(row=1, column=1)
        Label(key_frame, text="Key").grid(row=0, column=0)
        key_input = Entry(key_frame, width=8)
        key_input.grid(row=0, column=1)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(button_frame, text="Encrypt", command=lambda: Rail_fence_cipher.encrypt_data(plaintext_input.get("1.0", "end"), key_input.get(), ciphertext_input)).grid(
            row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Decrypt", command=lambda: Rail_fence_cipher.decrypt_data(ciphertext_input.get("1.0", "end"), key_input.get(), plaintext_input)).grid(
            row=0, column=1, padx=10, pady=10)
    # ?
    
    def encrypt_data(plaintext, key, ciphertext_input):
        # TODO: Validation
        ciphertext = encrypt(plaintext, int(key))
        ciphertext_input.delete("1.0", "end")
        ciphertext_input.insert("1.0", ciphertext)
    def decrypt_data(ciphertext, key, plaintext_input):
        # TODO: Validation
        plaintext = decrypt(ciphertext, int(key))
        plaintext_input.delete("1.0", "end")
        plaintext_input.insert("1.0", plaintext)
    