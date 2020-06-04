from main import mainframe, font_family, main_colour, button_colour, error_font, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, RAISED
from subpages import clear_screen
from cipher.mono_alphabet_cipher import encrypt, decrypt


class Mono_alphabet_cipher:
    def mono_alphabet_cipher_page():
        global Plaintext_error, Key_error, Ciphertext_error, Plaintext_input, Ciphertext_input, Key
        clear_screen(mainframe)
    # ? Title
        Label(
            mainframe,
            text="Monoalphabet Cipher",
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
        Plaintext_input = Text(
            plaintext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        Plaintext_input.grid(row=1, column=0, padx=10, pady=10)
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
        Ciphertext_input = Text(
            ciphertext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        Ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe, bg=main_colour)
        key_frame.grid(row=1, column=1, padx=20)
        Label(
            key_frame,
            text="Plaintext Alphabet",
            font=h2_font,
            background=main_colour).grid(row=3, column=0)
        Label(
            key_frame,
            text="Ciphertext Alphabet",
            font=h2_font,
            background=main_colour).grid(row=4, column=0)

        Message(
            key_frame,
            text="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            relief=RAISED,
            width=260,
            font=(font_family, 12),
            background="#ffffff").grid(row=3, column=1, columnspan=2)

        Key = Text(
            key_frame,
            width=27,
            height=1,
            font=(font_family, 12),
            relief="solid")
        Key.grid(row=4, column=1, columnspan=2)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe, bg=main_colour)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(
            button_frame,
            text="Encrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Mono_alphabet_cipher.encrypt_data()).grid(row=0, column=0, padx=10, pady=10)
        Button(
            button_frame,
            text="Decrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Mono_alphabet_cipher.decrypt_data()).grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Error Frame
        error_frame = Frame(mainframe, bg=main_colour)
        error_frame.grid(row=3, column=0, columnspan=3)
        Plaintext_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        Plaintext_error.grid(row=0, column=0)
        Key_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        Key_error.grid(row=1, column=0)
        Ciphertext_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        Ciphertext_error.grid(row=2, column=0)
    # ?

    def encrypt_data():
        key = Key.get("1.0", "end").strip('\n')
        plaintext = Plaintext_input.get("1.0", "end").strip('\n')
        # TODO: require validation
        valid = True
        sorted_key = sorted(key.upper())
        sorted_key = "".join(sorted_key)
    # ? Validate Key
        if sorted_key != "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # ? Some characters are missing or duplicated
            Key_error.config(text="Key has missing or duplicated letters.")
            valid = False
        else:
            Key_error.config(text="")
    # ?
    # ? Validate Plaintext
        if plaintext == "":
            # ? Plaintext should not be empty
            Plaintext_error.config(text="Plaintext cannot be empty.")
            valid = False
        else:
            Plaintext_error.config(text="")
    # ?
    # ? Clear Ciphertext Error
        Ciphertext_error.config(text="")
    # ?
        if valid:
            ciphertext = encrypt(key, plaintext)
            Ciphertext_input.delete("1.0", "end")
            Ciphertext_input.insert("1.0", ciphertext)

    def decrypt_data():
        key = Key.get("1.0", "end").strip('\n')
        ciphertext = Ciphertext_input.get("1.0", "end").strip('\n')
        # TODO: require validation
        valid = True
        sorted_key = sorted(key.upper())
        sorted_key = "".join(sorted_key)
    # ? Validate Key
        if sorted_key != "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # ? Some characters are missing or duplicated
            Key_error.config(text="Key has missing or duplicated letters.")
            valid = False
    # ?
    # ? Validate Ciphertext
        if ciphertext == "":
            # ? Ciphertext should not be empty
            Ciphertext_error.config(text="Ciphertext cannot be empty.")
            valid = False
    # ?
    # ? Clear Plaintext Error
        Plaintext_error.config(text="")
    # ?
        if valid:
            plaintext = decrypt(key, ciphertext)
            Plaintext_input.delete("1.0", "end")
            Plaintext_input.insert("1.0", plaintext)
