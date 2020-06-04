from tkinter import Label, Text, filedialog, Button, OptionMenu, StringVar, Frame, Entry
from subpages import clear_screen
from main import mainframe, font_family, main_colour, button_colour, error_font, h1_font, h2_font, h3_font, box_width
from cipher.shift_cipher import encrypt, decrypt


class Shift_cipher:
    def shift_cipher_page():
        global key_input, plaintext_input, ciphertext_input, key_error, plaintext_error, ciphertext_error
        clear_screen(mainframe)
    # ? Title
        Label(
            mainframe,
            text="Shift Cipher",
            font=h1_font,
            bg=main_colour).grid(row=0, column=0, columnspan=3)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe, bg=main_colour)
        plaintext_frame.grid(row=1, column=0)
        Label(
            plaintext_frame,
            text="Plaintext:",
            font=h2_font,
            background=main_colour).grid(row=0, column=0, padx=10, pady=10)
        plaintext_input = Text(
            plaintext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe, bg=main_colour)
        ciphertext_frame.grid(row=1, column=2)
        Label(
            ciphertext_frame,
            text="Ciphertext:",
            font=h2_font,
            background=main_colour).grid(row=0, column=0, padx=10, pady=10)
        ciphertext_input = Text(
            ciphertext_frame,
            width=box_width,
            height=10,
            font=h3_font,
            relief="solid")
        ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ? Key Frame
        key_frame = Frame(mainframe, bg=main_colour)
        key_frame.grid(row=1, column=1, padx=20)
        Label(
            key_frame,
            text="Key:",
            font=h2_font,
            background=main_colour).grid(row=0, column=0, padx=10, pady=10)
        key_input = Entry(
            key_frame,
            width=3,
            font=h2_font,
            relief="solid")
        key_input.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe, bg=main_colour)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(
            button_frame,
            text="Encrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Shift_cipher.encryption_shift()).grid(row=0, column=0, padx=10, pady=10)
        Button(
            button_frame,
            text="Decrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Shift_cipher.decryption_shift()).grid(
            row=0, column=1, padx=10, pady=10)
    # ? Error Frame
        error_frame = Frame(mainframe, bg=main_colour)
        error_frame.grid(row=3, column=0, columnspan=3)
        plaintext_error = Label(
            error_frame, text="", fg="red", font=error_font, background=main_colour)
        plaintext_error.grid(row=0, column=0)
        key_error = Label(error_frame, text="", fg="red",
                          font=error_font, background=main_colour)
        key_error.grid(row=1, column=0)
        ciphertext_error = Label(
            error_frame, text="", fg="red", font=error_font, background=main_colour)
        ciphertext_error.grid(row=2, column=0)
    # ?

    def encryption_shift():
        key = key_input.get()
        plaintext = plaintext_input.get("1.0", "end").strip('\n')
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
    # ? Clear Ciphertext Error
        ciphertext_error.config(text="")
    # ?
        if valid:
            ciphertext = encrypt(int(key), plaintext)
            ciphertext_input.delete("1.0", "end")
            ciphertext_input.insert("1.0", ciphertext)

    def decryption_shift():
        key = key_input.get()
        ciphertext = ciphertext_input.get("1.0", "end").strip('\n')
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
    # ?
    # ? Clear Plaintext Error
        plaintext_error.config(text="")
    # ?
        if valid:
            plaintext = decrypt(int(key), ciphertext)
            plaintext_input.delete("1.0", "end")
            plaintext_input.insert("1.0", plaintext)
