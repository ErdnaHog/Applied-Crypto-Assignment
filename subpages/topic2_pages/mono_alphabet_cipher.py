from main import mainframe
from tkinter import Label, Text, Button, Message, Frame, RAISED
from subpages import clear_screen
from cipher.mono_alphabet_cipher import encrypt, decrypt


class Mono_alphabet_cipher:
    def mono_alphabet_cipher_page():
        clear_screen(mainframe)
    # ? Title
        Label(mainframe, text="Monoalphabet Cipher").grid(
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
        Label(key_frame, text="Plaintext Alphabet").grid(row=3, column=0)
        Label(key_frame, text="Ciphertext Alphabet").grid(row=4, column=0)

        Message(key_frame, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", relief=RAISED,
                width=260).grid(row=3, column=1, columnspan=2)
        key = Text(key_frame, width=27, height=1)
        key.grid(row=4, column=1, columnspan=2)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(button_frame, text="Encrypt", command=lambda: Mono_alphabet_cipher.encrypt_data(key.get("1.0", "end").strip('\n'), plaintext_input.get("1.0", "end").strip('\n'), ciphertext_input, key_error, plaintext_error)).grid(
            row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Decrypt", command=lambda: Mono_alphabet_cipher.decrypt_data(key.get("1.0", "end").strip('\n'), ciphertext_input.get("1.0", "end").strip('\n'), plaintext_input, key_error, ciphertext_error)).grid(
            row=0, column=1, padx=10, pady=10)
    # ?
    # ? Error Frame
        error_frame = Frame(mainframe)
        error_frame.grid(row=3, column=0, columnspan=3)
        plaintext_error = Label(error_frame, text="", fg="red")
        plaintext_error.grid(row=0, column=0)
        key_error = Label(error_frame, text="", fg="red")
        key_error.grid(row=1, column=0)
        ciphertext_error = Label(error_frame, text="", fg="red")
        ciphertext_error.grid(row=2, column=0)
    # ?

    def encrypt_data(key, plaintext, ciphertext_input, key_error, plaintext_error):
        # TODO: require validation
        valid = True
        sorted_key = sorted(key.upper())
        sorted_key = "".join(sorted_key)
    # ? Validate Key
        if sorted_key != "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # ? Some characters are missing or duplicated
            key_error.config(text="Key has missing or duplicated letters.")
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
            ciphertext = encrypt(key, plaintext)
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decrypt_data(key, ciphertext, plaintext_input, key_error, ciphertext_error):
        # TODO: require validation
        valid = True
        sorted_key = sorted(key.upper())
        sorted_key = "".join(sorted_key)
    # ? Validate Key
        if sorted_key != "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # ? Some characters are missing or duplicated
            key_error.config(text="Key has missing or duplicated letters.")
            valid = False
    # ?
    # ? Validate Ciphertext
        if ciphertext == "":
            # ? Ciphertext should not be empty
            ciphertext_error.config(text="Ciphertext cannot be empty.")
            valid = False
    # ?
        if valid:
            plaintext = decrypt(key, ciphertext)
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
