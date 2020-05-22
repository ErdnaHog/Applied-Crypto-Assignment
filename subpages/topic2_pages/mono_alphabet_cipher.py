from tkinter import *
from subpages import clear_screen

class Mono_alphabet_cipher:
    def mono_alphabet_cipher_page():
        clear_screen(root)
        Label(root).grid(row=0, column=0)
        Label(root, text="Monoalphabet Cipher").grid(row=0, column=1, columnspan=2)
        plaintext = Label(root, text="Plaintext:")
        plaintext.grid(row=1, column=0, padx=10, pady=10)
        ciphertext = Label(root, text="Ciphertext:")
        ciphertext.grid(row=1, column=3, padx=10, pady=10)
        plaintext_input = Text(root, width=30, height=10)
        plaintext_input.grid(row=2, column=0, padx=10, pady=10)
        ciphertext_input = Text(root, width=30, height=10)
        ciphertext_input.grid(row=2, column=3, padx=10, pady=10)
        Button(root, text="Encrypt").grid(row=1, column=1, padx=10, pady=10)
        Button(root, text="Decrypt").grid(row=1, column=2, padx=10, pady=10)
        Label(root, text="Plaintext Alphabet").grid(row=3, column=0)
        Label(root, text="Ciphertext Alphabet").grid(row=4, column=0)
        Message(root, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", relief=RAISED, width=260).grid(row=3, column=1, columnspan=2)
        key = Text(root, width=27, height=1)
        key.grid(row=4, column=1, columnspan=2)
