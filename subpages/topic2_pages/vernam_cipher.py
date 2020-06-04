from main import mainframe, font_family, main_colour, button_colour, error_font, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, RAISED
from subpages import clear_screen
from cipher.vernam_cipher import encrypt, decrypt


class Vernam_cipher:
    def vernam_cipher_page():
        global key_input, plaintext_input, ciphertext_input, key_error, plaintext_error, ciphertext_error
        clear_screen(mainframe)
    # ? Title
        Label(
            mainframe,
            text="Vernam Cipher",
            font=h1_font,
            bg=main_colour).grid(row=0, column=0, columnspan=3)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe, bg=main_colour)
        plaintext_frame.grid(row=1, column=0)
        plaintext = Label(
            plaintext_frame,
            text="Plaintext:",
            font=h2_font,
            background=main_colour)
        plaintext.grid(row=0, column=0, padx=10, pady=10)
        plaintext_input = Text(
            plaintext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe, bg=main_colour)
        ciphertext_frame.grid(row=1, column=2)
        ciphertext = Label(
            ciphertext_frame,
            text="Ciphertext:",
            font=h2_font,
            background=main_colour)
        ciphertext.grid(row=0, column=0, padx=10, pady=10)
        ciphertext_input = Text(
            ciphertext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe, bg=main_colour)
        key_frame.grid(row=1, column=1)
        key = Label(
            key_frame,
            text="Key:",
            font=h2_font,
            background=main_colour)
        key.grid(row=0, column=0, padx=10, pady=10)
        key_input = Text(
            key_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        key_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe, bg=main_colour)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(
            button_frame,
            text="Encrypt",
            command=lambda: Vernam_cipher.encrypt_data()).grid(row=0, column=0, padx=10, pady=10)
        Button(
            button_frame,
            text="Decrypt",
            command=lambda: Vernam_cipher.decrypt_data()).grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Error Frame
        error_frame = Frame(mainframe, bg=main_colour)
        error_frame.grid(row=3, column=0, columnspan=3)
        plaintext_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        plaintext_error.grid(row=0, column=0)
        key_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        key_error.grid(row=1, column=0)
        ciphertext_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        ciphertext_error.grid(row=2, column=0)
    # ?

    def encrypt_data():
        key = key_input.get("1.0", "end").strip('\n')
        plaintext = plaintext_input.get("1.0", "end").strip('\n')
        valid = True
    # ? Validate Key
        if len(key) < len(plaintext):
            key_error.config(
                text="Length of key cannot be smaller than length of plaintext.")
            valid = False
        elif not key.isalpha():
            key_error.config(text="Key can only contain alphabets.")
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
    # ? Clear Ciphertext Error
        ciphertext_error.config(text="")
    # ?
        if valid:
            ciphertext = encrypt(key.upper(), plaintext.upper())
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decrypt_data():
        key = key_input.get("1.0", "end").strip('\n')
        ciphertext = ciphertext_input.get("1.0", "end").strip('\n')
        valid = True
    # ? Validate Key
        if len(key) < len(ciphertext):
            key_error.config(
                text="Length of key cannot be smaller than length of ciphertext.")
            valid = False
        elif not key.isalpha():
            key_error.config(text="Key can only contain alphabets.")
            valid = False
        else:
            key_error.config(text="")
    # ? Validate Ciphertext
        if ciphertext == "":
            ciphertext_error.config(text="Ciphertext cannot be empty.")
            valid = False
        else:
            ciphertext_error
    # ?
    # ? Clear Plaintext Error
        plaintext_error.config(text="")
    # ?
        if valid:
            plaintext = decrypt(key.upper(), ciphertext.upper())
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
