from main import mainframe, root
from subpages import clear_screen
from tkinter import Label, Text, filedialog, Button, OptionMenu, StringVar
from cipher.aes import get_random_bytes, encrypt


class Topic3:
    def clear_inputs(cipher_mode, key_size, plaintext, ciphertext_file, create_ciphertext_file):
        pass

    def aes_page():
        clear_screen(mainframe)

        # create a tkinter variable called cipher_mode
        cipher_mode = StringVar(root)
        # create a tkinter variable called key_size
        key_size = StringVar(root)
        # create a tkinter variable called filename
        ciphertext_file = StringVar(root)

        # dictionary with different choices of cipher_mode
        cipher_mode_choices = {'ECB', 'CBC', 'CFB', 'OFB'}
        # dictionary with different choices of  key_size
        key_size_choices = {'128', '192', '256'}

        # set default values of key_size and cipher_mode
        cipher_mode.set('CBC')
        key_size.set('192')

        Label(mainframe, text="AES").grid(
            row=0, column=1, columnspan=2)
        Label(mainframe, text="Cipher Mode:").grid(
            row=2, column=1)
        Label(mainframe, text="Key Size:").grid(
            row=3, column=1)
        plaintext = Label(mainframe, text="Plaintext:")
        plaintext.grid(row=1, column=0, padx=10, pady=10)

        ciphertext = Label(mainframe, text="Ciphertext:")
        ciphertext.grid(row=1, column=3, padx=10, pady=10, columnspan=2)

        plaintext_input = Text(mainframe, width=30, height=10)
        plaintext_input.grid(row=2, column=0, padx=10, pady=10, rowspan=3)

        Button(mainframe, text="Encrypt", command=lambda: Topic3.encrypt_data(plaintext_input.get("1.0", "end").strip('\n'), key_size.get(), cipher_mode.get(), ciphertext_file.get())).grid(
            row=1, column=1, padx=10, pady=10)
        Button(mainframe, text="Decrypt").grid(
            row=1, column=2, padx=10, pady=10)

        cipher_mode_option = OptionMenu(
            mainframe, cipher_mode, *cipher_mode_choices)
        cipher_mode_option.grid(row=2, column=2, padx=10, pady=10)

        key_size_option = OptionMenu(mainframe, key_size, *key_size_choices)
        key_size_option.grid(row=3, column=2, padx=10, pady=10)

        filename_label = Label(mainframe, text="Filename")
        filename_label.grid(row=2, column=3, padx=20, pady=20, columnspan=2)
        Button(mainframe, text="Choose A File", command=lambda: Topic3.choose_file(ciphertext_file, filename_label)).grid(
            row=3, column=3, padx=20, pady=10)
        Button(mainframe, text="Create A File", command=lambda: Topic3.create_file(ciphertext_file, filename_label)).grid(
            row=3, column=4, padx=20, pady=10)

    def encrypt_data(plaintext, key_size, cipher_mode, ciphertext_file):
        # TODO: validation
        key = get_random_bytes(int(int(key_size)/8))
        print(key)
        encrypt(key, plaintext.encode("utf8"), ciphertext_file, cipher_mode)

    # TODO: decrypt data
    def decrypt_data():
        pass

    def choose_file(ciphertext_file, filename_label):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetype=(("binary files", ".bin"), ("all files", "*.*")))
        filename_label.configure(text=filename)
        ciphertext_file.set(filename)

    def create_file(ciphertext_file, filename_label):
        filename = filedialog.asksaveasfile(
            initialdir="/", title="Create Binary File", filetype=(("binary files", ".bin"), ("all files", "*.*")), defaultextension=(("binary files", ".bin"), ("all files", "*.*")))
        filename_label.configure(text=filename.name)
        ciphertext_file.set(filename)
