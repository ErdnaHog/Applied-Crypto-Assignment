from main import mainframe, root
from subpages import clear_screen
from tkinter import Label, Text, filedialog, Button, OptionMenu, StringVar, Frame
from cipher.aes import get_random_bytes, encrypt, decrypt


class Topic3:
    def clear_inputs(cipher_mode, key_size, plaintext, ciphertext_file, create_ciphertext_file):
        pass

    def aes_page():
        clear_screen(mainframe)
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
        Label(mainframe, text="AES").grid(
            row=0, column=1, columnspan=2)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe)
        plaintext_frame.grid(row=1, column=0, rowspan=4)
        Label(plaintext_frame, text="Plaintext:").grid(row=0, column=0, padx=10, pady=10)        
        plaintext_input = Text(plaintext_frame, width=20, height=10)
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe)
        key_frame.grid(row=1, column=1, rowspan=2)
        Label(key_frame, text="Key File:").grid(
            row=0, column=1, columnspan=2)
        key_file_label = Label(key_frame, text="")
        key_file_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        Button(key_frame, text="Choose A File", command=lambda: Topic3.choose_file(key_file, key_file_label)).grid(
            row=2, column=1, padx=10, pady=10)
        Button(key_frame, text="Create A File", command=lambda: Topic3.create_file(key_file, key_file_label)).grid(
            row=2, column=2, padx=10, pady=10)
    # ?
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe)
        ciphertext_frame.grid(row=1, column=3, rowspan=2)
        Label(ciphertext_frame, text="Ciphertext File:").grid(row=0, column=0, columnspan=2)
        ciphertext_file_label = Label(ciphertext_frame, text="")
        ciphertext_file_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        Button(ciphertext_frame, text="Choose A File", command=lambda: Topic3.choose_file(ciphertext_file, ciphertext_file_label)).grid(
            row=2, column=0, padx=20, pady=10)
        Button(ciphertext_frame, text="Create A File", command=lambda: Topic3.create_file(ciphertext_file, ciphertext_file_label)).grid(
            row=2, column=1, padx=20, pady=10)
    # ?
    # ? Key Mode Frame
        key_mode_frame = Frame(mainframe)
        key_mode_frame.grid(row=3, column=1)
        Label(key_mode_frame, text="Cipher Mode:").grid(
            row=0, column=0)
        cipher_mode_option = OptionMenu(key_mode_frame, cipher_mode, *cipher_mode_choices)
        cipher_mode_option.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Key Size Frame
        key_size_frame = Frame(mainframe)
        key_size_frame.grid(row=4, column=1)
        Label(key_size_frame, text="Key Size:").grid(
            row=0, column=0)
        key_size_option = OptionMenu(key_size_frame, key_size, *key_size_choices)
        key_size_option.grid(row=0, column=1, padx=10, pady=10)
    # ?
    # ? Buttons Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=5, column=1)
        Button(button_frame, text="Encrypt", command=lambda: Topic3.encrypt_data(plaintext_input.get("1.0", "end").strip('\n'), key_size.get(), cipher_mode.get(), ciphertext_file.get(), key_file.get(), plaintext_input_error, key_file_error, ciphertext_file_error)).grid(
            row=1, column=1, padx=10, pady=10)
        Button(button_frame, text="Decrypt", command=lambda: Topic3.decrypt_data(plaintext_input, cipher_mode.get(), ciphertext_file.get(), key_file.get())).grid(
            row=1, column=2, padx=10, pady=10)
    # ?
    # ? Errors Frame
        error_frame = Frame(mainframe)
        error_frame.grid(row=6, column=1)
        plaintext_input_error = Label(error_frame, text="", fg="red")
        plaintext_input_error.grid(row=0, column=0)
        key_file_error = Label(error_frame, text="", fg="red")
        key_file_error.grid(row=1, column=0)
        ciphertext_file_error = Label(error_frame, text="", fg="red")
        ciphertext_file_error.grid(row=2, column=0)
        cipher_mode_error = Label(error_frame, text="", fg="red")
        cipher_mode_error.grid(row=3, column=0)
    # ?

    def encrypt_data(plaintext, key_size, cipher_mode, ciphertext_file, key_file, plaintext_input_error, key_file_error, ciphertext_file_error):
        valid = True
    # ? Validate Plaintext Input
        if plaintext == "":
            plaintext_input_error.config(text="Plaintext cannot be empty")
            valid = False
    # ?
    # ? Validate Key File
        if key_file == "":
            # ! No file chosen
            key_file_error.config(text="No Key file is chosen.")
            valid = False
        elif key_file[-4:-1] != ".bin":
            # !  File is not binary
            key_file_error.config(text="Key file is not a binary file.")
            valid = False
    # ?
    # ? Validate Ciphertext File
        if ciphertext_file == "":
            # ! No file chosen
            ciphertext_file_error.config(text="No ciphertext file is chosen.")
            valid = False
        elif ciphertext_file[-4:-1] != ".bin":
            # !  File is not binary
            ciphertext_file_error.config(text="Key ciphertext is not a binary file.")
            valid = False
    # ?
        if valid:
            key = get_random_bytes(int(int(key_size)/8))
            with open(key_file, "wb") as file:
                file.write(key)
            encrypt(key, plaintext.encode("utf8"), ciphertext_file, cipher_mode)

    def decrypt_data(plaintext_input, cipher_mode, ciphertext_file, key_file, key_file_error, ciphertext_file_error, cipher_mode_error):
        valid = True
    # ? Validate Key File
        if key_file == "":
            # ! No file chosen
            key_file_error.config(text="No Key file is chosen.")
            valid = False
        elif key_file[-4:-1] != ".bin":
            # !  File is not binary
            key_file_error.config(text="Key file is not a binary file.")
            valid = False
    # ?
    # ? Validate Ciphertext File
        if ciphertext_file == "":
            # ! No file chosen
            ciphertext_file_error.config(text="No ciphertext file is chosen.")
            valid = False
        elif ciphertext_file[-4:-1] != ".bin":
            # !  File is not binary
            ciphertext_file_error.config(text="Key ciphertext is not a binary file.")
            valid = False
    # ?
        if valid:
            with open(key_file, "rb") as file:
                key = file.read()
            try:
                plaintext = decrypt(key, ciphertext_file, cipher_mode).decode("utf8")  
                plaintext_input.delete("1.0", "end")
                plaintext_input.insert("1.0", plaintext)
            except:
                cipher_mode_error.config(text="Wrong Cipher Mode")

    def choose_file(file_variable, filename_label):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetype=(("binary files", ".bin"), ("all files", "*.*")))
        filename_label.configure(text=filename)
        file_variable.set(filename)

    def create_file(file_variable, filename_label):
        filename = filedialog.asksaveasfile(
            initialdir="/", title="Create Binary File", filetype=(("binary files", ".bin"), ("all files", "*.*")), defaultextension=(("binary files", ".bin"), ("all files", "*.*")))
        filename_label.configure(text=filename.name)
        file_variable.set(filename)