from main import mainframe
from tkinter import *
from subpages import clear_screen


class Mono_alphabet_cipher:
    def mono_alphabet_cipher_page():
        clear_screen(mainframe)

        Label(mainframe, text="Monoalphabet Cipher").grid(
            row=0, column=1, columnspan=2)
        plaintext = Label(mainframe, text="Plaintext:")
        plaintext.grid(row=1, column=0, padx=10, pady=10)

        ciphertext = Label(mainframe, text="Ciphertext:")
        ciphertext.grid(row=1, column=3, padx=10, pady=10)

        plaintext_input = Text(mainframe, width=30, height=10)
        plaintext_input.grid(row=2, column=0, padx=10, pady=10)

        ciphertext_input = Text(mainframe, width=30, height=10)
        ciphertext_input.grid(row=2, column=3, padx=10, pady=10)

        Button(mainframe, text="Encrypt").grid(
            row=1, column=1, padx=10, pady=10)
        Button(mainframe, text="Decrypt").grid(
            row=1, column=2, padx=10, pady=10)

        Label(mainframe, text="Plaintext Alphabet").grid(row=3, column=0)
        Label(mainframe, text="Ciphertext Alphabet").grid(row=4, column=0)

        Message(mainframe, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", relief=RAISED,
                width=260).grid(row=3, column=1, columnspan=2)
        key = Text(mainframe, width=27, height=1)
        key.grid(row=4, column=1, columnspan=2)
