from tkinter import Label, Text, filedialog, Button, OptionMenu, StringVar, Frame, Entry
from subpages import clear_screen
from main import mainframe
from cipher.shift_cipher import encrypt, decrypt


class Shift_cipher:
    def shift_cipher_page():
        clear_screen(mainframe)
    # ? Title
        Label(mainframe, text="Shift Cipher").grid(
            row=0, column=0, columnspan=3)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe)
        plaintext_frame.grid(row=1, column=0)
        Label(plaintext_frame, text="Plaintext:").grid(
            row=0, column=0, padx=10, pady=10)
        plaintext_input = Text(plaintext_frame, width=20, height=10)
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe)
        ciphertext_frame.grid(row=1, column=2)
        Label(ciphertext_frame, text="Ciphertext:").grid(
            row=0, column=0, padx=10, pady=10)
        ciphertext_input = Text(ciphertext_frame, width=20, height=10)
        ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ? Key Frame
        key_frame = Frame(mainframe)
        key_frame.grid(row=1, column=1)
        Label(key_frame, text="Key:").grid(row=0, column=0, padx=10, pady=10)
        keytext_input = Entry(key_frame, width=3)
        keytext_input.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(button_frame, text="Encrypt", command=lambda: Shift_cipher.encryption_shift(keytext_input.get(
        ), plaintext_input.get("1.0", "end").strip('\n'), ciphertext_input, key_error, plaintext_error)).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Decrypt", command=lambda: Shift_cipher.decryption_shift(keytext_input.get(
        ), ciphertext_input.get("1.0", "end").strip('\n'), plaintext_input, key_error, ciphertext_error)).grid(
            row=0, column=1, padx=10, pady=10)
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

    def encryption_shift(key, plaintext, ciphertext_input, key_error, plaintext_error):
        valid = True
    # ? Validate Key
        if not key.isdigit():
            key_error.config(text="Key must be a positive integer.")
            valid = False

        elif int(key) > 26:
            key_error.config(text="Key cannot be larger than 26.")
            valid = False

        else:
            key_error.config(text="")
    # ?
    # ? Validate Plaintext
        if plaintext == "":
            plaintext_error.config(text="Plaintext cannot be empty.")
            valid = False
        else:
            plaintext_error.config(text="")
    # ?
        if valid:
            ciphertext = encrypt(int(key), plaintext)
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decryption_shift(key, ciphertext, plaintext_input, key_error, ciphertext_error):
        valid = True
    # ? Validate Key
        if not key.isdigit():
            key_error.config(text="Key must be a positive integer.")
            valid = False

        elif int(key) > 26:
            key_error.config(text="Key cannot be larger than 26.")
            valid = False

        else:
            key_error.config(text="")
    # ?
    # ? Validate Ciphertext
        if ciphertext == "":
            ciphertext_error.config(text="Ciphertext cannot be empty.")
            valid = False
        else:
            ciphertext_error.config(text="")

        if valid:
            plaintext = decrypt(int(key), ciphertext)
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
