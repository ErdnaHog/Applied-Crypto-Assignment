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
        Label(key_frame, text="Key (number of rows)").grid(row=0, column=0)
        key_input = Entry(key_frame, width=8)
        key_input.grid(row=0, column=1)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(button_frame, text="Encrypt", command=lambda: Rail_fence_cipher.encrypt_data(plaintext_input.get("1.0", "end").strip('\n'), key_input.get(), ciphertext_input, key_error, plaintext_error)).grid(
            row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Decrypt", command=lambda: Rail_fence_cipher.decrypt_data(ciphertext_input.get("1.0", "end").strip('\n'), key_input.get(), plaintext_input, key_error, ciphertext_error)).grid(
            row=0, column=1, padx=10, pady=10)
    # ?
    # ? Error Frame
        error_frame = Frame(mainframe)
        error_frame.grid(row=3, column=0, columnspan=3)
        key_error = Label(error_frame, text="", fg="red")
        key_error.grid(row=0, column=0)
        plaintext_error = Label(error_frame, text="", fg="red")
        plaintext_error.grid(row=1, column=0)
        ciphertext_error = Label(error_frame, text="", fg="red")
        ciphertext_error.grid(row=2, column=0)
    # ?

    def encrypt_data(plaintext, key, ciphertext_input, key_error, plaintext_error):
        valid = True
    # ? Validate Key
        if not key.isdigit():
            # ? Key is not a digit
            key_error.config(text="Key must be a positive integer.")
            valid = False
        elif int(key) >= len(plaintext):
            # ? Key length is larger or equal to len of plaintext which is invalid since number of rows cannot be larger or equal to plaintext
            key_error.config(
                text="Key value cannot be larger or equal to length of plaintext.")
            valid = False
        else:
            key_error.config(text="")
    # ?
    # ? Validate Plaintext
        if plaintext == "":
            # ? Plaintext should not be empty
            plaintext_error.config(text="Plaintext cannot be empty.")
            valid = False
        else:
            plaintext_error.config(text="")
    # ?
        if valid:
            ciphertext = encrypt(int(key), plaintext)
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decrypt_data(ciphertext, key, plaintext_input, key_error, ciphertext_error):
        valid = True
    # ? Validate Key
        if not key.isdigit():
            # ? Key is not a digit
            key_error.config(text="Key must be a positive integer.")
            valid = False
        elif int(key) >= len(ciphertext):
            # ? Key length is larger or equal to len of ciphertext which is invalid since number of rows cannot be larger or equal to ciphertext
            key_error.config(
                text="Key value cannot be larger or equal to length of ciphertext.")
        else:
            key_error.config(text="")
    # ?
    # ? Validate Ciphertext
        if ciphertext == "":
            # ? Ciphertext should not be empty
            ciphertext_error.config(text="Plaintext cannot be empty.")
            valid = False
        else:
            ciphertext_error.config(text="")
    # ?
        if valid:
            plaintext = decrypt(int(key), ciphertext)
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
