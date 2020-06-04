from main import mainframe, root, font_family, main_colour, button_colour, error_font, h1_font, h2_font, h3_font, box_width, button_colour2
from subpages import clear_screen
from tkinter import Label, Text, filedialog, Button, OptionMenu, StringVar, Frame
from cipher.aes import get_random_key, encrypt, decrypt


class Topic3:
    def clear_inputs(cipher_mode, key_size, plaintext, ciphertext_file, create_ciphertext_file):
        pass

    def aes_page():
        clear_screen(mainframe)
        global plaintext_input, key_size, cipher_mode, ciphertext_file, key_file, plaintext_input_error, key_file_error, cipher_mode_error, ciphertext_file_error, success
    # ? Tkinter Variables
        # * create a tkinter variable called cipher_mode
        cipher_mode = StringVar(root)
        # * create a tkinter variable called key_size
        key_size = StringVar(root)
        # * create a tkinter variable called ciphertext_file
        ciphertext_file = StringVar(root)
        # * createa tkinter variable called key_file
        key_file = StringVar(root)
    # ?
    # ? Choices
        # * dictionary with different choices of cipher_mode
        cipher_mode_choices = {'ECB', 'CBC', 'CFB', 'OFB'}
        # * dictionary with different choices of  key_size
        key_size_choices = {'128', '192', '256'}
    # ?
    # ? Setting default value in dropdown
        # set default values of key_size and cipher_mode
        cipher_mode.set('CBC')
        key_size.set('192')
    # ?
    # ? Title
        Label(
            mainframe,
            text="AES",
            font=h1_font,
            bg=main_colour).grid(row=0, column=0, columnspan=5)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe, bg=main_colour)
        plaintext_frame.grid(row=1, column=0, rowspan=4)
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
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe, bg=main_colour)
        key_frame.grid(row=1, column=1, rowspan=2)
        Label(
            key_frame,
            text="Key File:",
            font=h2_font,
            background=main_colour,
            width=box_width).grid(row=0, column=1, columnspan=2)
        key_file_label = Label(
            key_frame,
            text="",
            font=h3_font,
            background=main_colour)
        key_file_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        Button(
            key_frame,
            text="Choose A File",
            font=(font_family, 12),
            background=button_colour2,
            command=lambda: Topic3.choose_file(key_file, key_file_label)).grid(
            row=2, column=1, padx=10, pady=10)
        Button(
            key_frame,
            text="Create A File",
            font=(font_family, 12),
            background=button_colour2,
            command=lambda: Topic3.create_file(key_file, key_file_label)).grid(
            row=2, column=2, padx=10, pady=10)
    # ?
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe, bg=main_colour)
        ciphertext_frame.grid(row=1, column=3, rowspan=2)
        Label(
            ciphertext_frame,
            text="Ciphertext File:",
            font=h2_font,
            background=main_colour,
            width=box_width).grid(row=0, column=0, columnspan=2)
        ciphertext_file_label = Label(
            ciphertext_frame,
            text="",
            font=h3_font,
            background=main_colour)
        ciphertext_file_label.grid(
            row=1, column=0, padx=10, pady=10, columnspan=2)
        Button(
            ciphertext_frame,
            text="Choose A File",
            font=(font_family, 12),
            background=button_colour2,
            command=lambda: Topic3.choose_file(ciphertext_file, ciphertext_file_label)).grid(
            row=2, column=0, padx=20, pady=10)
        Button(
            ciphertext_frame,
            text="Create A File",
            font=(font_family, 12),
            background=button_colour2,
            command=lambda: Topic3.create_file(ciphertext_file, ciphertext_file_label)).grid(
            row=2, column=1, padx=20, pady=10)
    # ?
    # ? Key Mode Frame
        key_mode_frame = Frame(mainframe, bg=main_colour)
        key_mode_frame.grid(row=3, column=1)
        Label(
            key_mode_frame,
            text="Cipher Mode:",
            font=h2_font,
            background=main_colour).grid(row=0, column=0)
        cipher_mode_option = OptionMenu(
            key_mode_frame,
            cipher_mode,
            *cipher_mode_choices)
        cipher_mode_option.config(bg=button_colour2, relief="solid")
        cipher_mode_option.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Key Size Frame
        key_size_frame = Frame(mainframe, bg=main_colour)
        key_size_frame.grid(row=4, column=1)
        Label(
            key_size_frame,
            text="Key Size:",
            font=h2_font,
            background=main_colour).grid(row=0, column=0)
        key_size_option = OptionMenu(
            key_size_frame,
            key_size,
            *key_size_choices)
        key_size_option.config(bg=button_colour2, relief="solid")
        key_size_option.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Buttons Frame
        button_frame = Frame(mainframe, bg=main_colour)
        button_frame.grid(row=5, column=1)
        Button(
            button_frame,
            text="Encrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Topic3.encrypt_data()).grid(
            row=1, column=1, padx=10, pady=10)
        Button(
            button_frame,
            text="Decrypt",
            font=(font_family, 12),
            background=button_colour,
            command=lambda: Topic3.decrypt_data()).grid(
            row=1, column=2, padx=10, pady=10)
    # ?
    # ? Errors Frame
        error_frame = Frame(mainframe, bg=main_colour)
        error_frame.grid(row=6, column=1)
        plaintext_input_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        plaintext_input_error.grid(row=0, column=0)
        key_file_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        key_file_error.grid(row=1, column=0)
        ciphertext_file_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        ciphertext_file_error.grid(row=2, column=0)
        cipher_mode_error = Label(
            error_frame,
            text="",
            font=error_font,
            fg="red",
            background=main_colour)
        cipher_mode_error.grid(row=3, column=0)
    # ?
    # ? Response Frame
        response_frame = Frame(mainframe, bg=main_colour)
        response_frame.grid(row=7, column=1)
        success = Label(
            response_frame,
            text="",
            font=(font_family, 13, 'bold'),
            background=main_colour
        )
        success.grid(row=0, column=0, pady=5)

    def encrypt_data():
        plaintext = plaintext_input.get("1.0", "end").strip('\n')
        Key_file = key_file.get()
        Cipher_mode = cipher_mode.get()
        Ciphertext_file = ciphertext_file.get()
        valid = True
    # ? Validate Plaintext Input
        if plaintext == "":
            plaintext_input_error.config(text="Plaintext cannot be empty.")
            valid = False
        else:
            plaintext_input_error.config(text="")
    # ?
    # ? Validate Key File
        if Key_file == "":
            # ! No file chosen
            key_file_error.config(text="No Key file is chosen.")
            valid = False
        elif Key_file[-4:] != ".bin":
            # !  File is not binary
            key_file_error.config(text="Key file is not a binary file.")
            valid = False
        else:
            key_file_error.config(text="")
    # ?
    # ? Validate Ciphertext File
        if Ciphertext_file == "":
            # ! No file chosen
            ciphertext_file_error.config(text="No ciphertext file is chosen.")
            valid = False
        elif Ciphertext_file[-4:] != ".bin":
            # ! File is not binary
            ciphertext_file_error.config(
                text="Key ciphertext is not a binary file.")
            valid = False
        elif Ciphertext_file == Key_file:
            # ! Ciphertext file != Key file
            key_file_error.config(
                text="Key file cannot be the same as ciphertext file.")
            ciphertext_file_error.config(
                text="Ciphertext file cannot be same as key file.")
            valid = False
        else:
            ciphertext_file_error.config(text="")
    # ?
    # ? Clear Cipher Mode Error
        cipher_mode_error.config(text="")
        if valid:
            key = get_random_key(int(int(key_size.get())/8))
            with open(Key_file, "wb") as file:
                file.write(key)
            encrypt(key, plaintext.encode("utf8"),
                    Ciphertext_file, Cipher_mode)
            success.config(text="Encryption success.", fg="green")
        else:
            success.config(text="Encryption failed.", fg="red")

    def decrypt_data():

        Key_file = key_file.get()
        Cipher_mode = cipher_mode.get()
        Ciphertext_file = ciphertext_file.get()
        valid = True
    # ? Validate Key File
        if Key_file == "":
            # ! No file chosen
            key_file_error.config(text="No Key file is chosen.")
            valid = False
        elif Key_file[-4:] != ".bin":
            # !  File is not binary
            key_file_error.config(text="Key file is not a binary file.")
            valid = False
        else:
            key_file_error.config(text="")
    # ?
    # ? Validate Ciphertext File
        if Ciphertext_file == "":
            # ! No file chosen
            ciphertext_file_error.config(text="No ciphertext file is chosen.")
            valid = False
        elif Ciphertext_file[-4:] != ".bin":
            # !  File is not binary
            ciphertext_file_error.config(
                text="Key ciphertext is not a binary file.")
            valid = False
        elif Ciphertext_file == Key_file:
            # ! Ciphertext file != Key file
            key_file_error.config(
                text="Key file cannot be the same as ciphertext file.")
            ciphertext_file_error.config(
                text="Ciphertext file cannot be same as key file.")
            valid = False
        else:
            ciphertext_file_error.config(text="")
    # ?
    # ? Clear Plaintext Error
        plaintext_input_error.config(text="")
    # ?
        if valid:
            with open(Key_file, "rb") as file:
                key = file.read()
            try:
                plaintext = decrypt(key, Ciphertext_file,
                                    Cipher_mode).decode("utf8")
                plaintext_input.delete("1.0", "end")
                plaintext_input.insert("1.0", plaintext)
                success.config(text="Decryption success.", fg="green")
            except:
                cipher_mode_error.config(
                    text="Wrong Cipher Mode or Wrong size key or No ciphertext.")
                success.config(text="Decryption failed.", fg="red")
        else:
            success.config(text="Decryption failed.", fg="red")

    def choose_file(file_variable, filename_label):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetype=(("binary files", ".bin"), ("all files", "*.*")))
        filename_label.configure(text=filename)
        file_variable.set(filename)

    def create_file(file_variable, filename_label):
        filename = filedialog.asksaveasfile(
            initialdir="/", title="Create Binary File", filetype=(("binary files", ".bin"), ("all files", "*.*")), defaultextension=(("binary files", ".bin"), ("all files", "*.*")))
        try:
            filename_label.configure(text=filename.name)
            file_variable.set(filename.name)
        except:
            file_variable.set("")
        print(file_variable)
