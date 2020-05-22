from tkinter import *
from subpages import clear_screen
from main import mainframe
from cipher.shift_cipher import encrypt, decrypt


class Shift_cipher:
    def shift_cipher_page():
        clear_screen(mainframe)
        Label(mainframe, text="Shift Cipher").grid(
            row=0, column=1, columnspan=2)
        Label(mainframe, text="Plaintext:").grid(
            row=1, column=0, padx=10, pady=10)
        Label(mainframe, text="Ciphertext:").grid(
            row=1, column=3, padx=10, pady=10)
        Label(mainframe, text="Key:").grid(row=2, column=1, padx=10, pady=10)
        plaintext_input = Text(mainframe, width=20, height=10)
        plaintext_input.grid(row=2, column=0, padx=10, pady=10)
        ciphertext_input = Text(mainframe, width=20, height=10)
        ciphertext_input.grid(row=2, column=3, padx=10, pady=10)
        keytext_input = Entry(mainframe, width=3)
        keytext_input.grid(row=2, column=2, padx=10, pady=10)
        Button(mainframe, text="Encrypt", command=lambda: Shift_cipher.encryption_shift(keytext_input.get(
        ), plaintext_input.get("1.0", "end"), ciphertext_input)).grid(row=1, column=1, padx=10, pady=10)
        Button(mainframe, text="Decrypt", command=lambda: Shift_cipher.decryption_shift(keytext_input.get(
        ), ciphertext_input.get("1.0", "end"), plaintext_input)).grid(
            row=1, column=2, padx=10, pady=10)
        Button(mainframe, text="Clear", command=lambda: Shift_cipher.clear_inputs(keytext_input, plaintext_input, ciphertext_input)).grid(
            row=5, column=1, padx=10, pady=10, columnspan=2)

    def encryption_shift(key, plaintext, ciphertext_input):
        valid = True
        if not key.isdigit():
            integer_error = Label(
                mainframe, text="Key must be a positive integer", fg="red")
            integer_error.grid(row=3, column=1, columnspan=2)
            valid = False

        elif int(key) > 26:
            integer_error = Label(
                mainframe, text="Key cannot be larger than 26", fg="red")
            integer_error.grid(row=3, column=1, columnspan=2)
            valid = False

        elif mainframe.grid_slaves(3, 1):
            mainframe.grid_slaves(3, 1)[0].grid_forget()

        if plaintext == "\n":
            plaintext_error = Label(
                mainframe, text="Plaintext cannot be empty.", fg="red")
            plaintext_error.grid(row=4, column=1, columnspan=2)
            valid = False

        elif mainframe.grid_slaves(4, 1):
            mainframe.grid_slaves(4, 1)[0].grid_forget()

        if valid:
            ciphertext = encrypt(int(key), plaintext)
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decryption_shift(key, ciphertext, plaintext_input):
        valid = True
        if not key.isdigit():
            integer_error = Label(
                mainframe, text="Key must be a positive integer", fg="red")
            integer_error.grid(row=3, column=1, columnspan=2)
            valid = False

        elif int(key) > 26:
            integer_error = Label(
                mainframe, text="Key cannot be larger than 26", fg="red")
            integer_error.grid(row=3, column=1, columnspan=2)
            valid = False

        elif mainframe.grid_slaves(3, 1):
            mainframe.grid_slaves(3, 1)[0].grid_forget()

        if ciphertext == "\n":
            ciphertext_error = Label(
                mainframe, text="Plaintext cannot be empty.", fg="red")
            ciphertext_error.grid(row=4, column=1, columnspan=2)
            valid = False

        elif mainframe.grid_slaves(4, 1):
            mainframe.grid_slaves(4, 1)[0].grid_forget()

        if valid:
            plaintext = decrypt(int(key), ciphertext)
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
