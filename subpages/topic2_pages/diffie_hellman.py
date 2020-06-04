from main import mainframe, font_family, main_colour, button_colour, error_font, h1_font, h2_font, h3_font, box_width, root
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry
from subpages import clear_screen
from cipher.diffie_hellman import is_prime, step_one, step_two
import time


class Diffie_hellman:
    def diffie_hellman_page():
        global g_number, n_number, alice_number, bob_number, g_number_error, n_number_error, alice_number_error, bob_number_error, alice_key, bob_key

        alice_number = StringVar(mainframe)
        bob_number = StringVar(mainframe)
        g_number = StringVar(mainframe)
        n_number = StringVar(mainframe)

        clear_screen(mainframe)
    # ? Title
        Label(
            mainframe,
            text="Diffie Hellman Key Exchange",
            font=h1_font,
            bg=main_colour).grid(row=0, column=0, columnspan=5)
    # ?
    # ? Alice Frame
        alice_frame = Frame(mainframe, bg=main_colour)
        alice_frame.grid(row=1, column=0, rowspan=3)
        Label(
            alice_frame,
            text="Alice",
            font=h2_font,
            bg=main_colour
        ).grid(row=0, column=0, columnspan=2)
        Label(
            alice_frame,
            text="Any random number:",
            font=h3_font,
            bg=main_colour
        ).grid(row=1, column=0)
        Entry(
            alice_frame,
            width=10,
            font=h3_font,
            relief="solid",
            textvariable=alice_number
        ).grid(row=1, column=1)
        alice_key = Label(
            alice_frame,
            width=box_width,
            font=h3_font,
            bg=main_colour,
            wraplength=350
        )
        alice_key.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    # ? Bob Frame
        bob_frame = Frame(mainframe, bg=main_colour)
        bob_frame.grid(row=1, column=3, rowspan=3)
        Label(
            bob_frame,
            text="Bob",
            font=h2_font,
            bg=main_colour
        ).grid(row=0, column=0, columnspan=2)
        Label(
            bob_frame,
            text="Any random number:",
            font=h3_font,
            bg=main_colour
        ).grid(row=1, column=0)
        Entry(
            bob_frame,
            width=10,
            font=h3_font,
            relief="solid",
            textvariable=bob_number
        ).grid(row=1, column=1)
        bob_key = Label(
            bob_frame,
            width=box_width,
            font=h3_font,
            bg=main_colour,
            wraplength=350
        )
        bob_key.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    # ? Shared Number Frame
        shared_number_frame = Frame(mainframe, bg=main_colour)
        shared_number_frame.grid(row=1, column=1, padx=30, pady=20)
        Label(
            shared_number_frame,
            text="G (any prime number):",
            font=h3_font,
            bg=main_colour
        ).grid(row=0, column=0)
        Entry(
            shared_number_frame,
            width=8,
            font=h3_font,
            relief="solid",
            textvariable=g_number
        ).grid(row=0, column=1)
        Label(
            shared_number_frame,
            text="N (any prime number):",
            font=h3_font,
            bg=main_colour
        ).grid(row=1, column=0)
        Entry(
            shared_number_frame,
            width=8,
            font=h3_font,
            relief="solid",
            textvariable=n_number
        ).grid(row=1, column=1)

    # ? Button Frame
        button_frame = Frame(mainframe, bg=main_colour)
        button_frame.grid(row=2, column=1, pady=(10, 0))
        Button(
            button_frame,
            text="Generate Key",
            font=(font_family, 12),
            bg=button_colour,
            command=Diffie_hellman.generate_key
        ).grid(row=0, column=0)
    # ? Error Frame
        error_frame = Frame(mainframe, bg=main_colour)
        error_frame.grid(row=3, column=0, columnspan=5)
        g_number_error = Label(error_frame)
        n_number_error = Label(error_frame)
        alice_number_error = Label(error_frame)
        bob_number_error = Label(error_frame)
        list_of_label_error = [
            g_number_error, n_number_error, alice_number_error, bob_number_error]
        i = 0
        for label_error in list_of_label_error:
            label_error.config(
                font=error_font,
                fg="red",
                background=main_colour
            )
            label_error.grid(row=i, column=0)
            i += 1

    def generate_key():
        valid = 0
        # ? Validate G
        if g_number.get() == "":
            g_number_error.config(text="G Number must not be empty.")
        elif not g_number.get().isdigit():
            g_number_error.config(text="G Number must be a prime number.")
        elif not is_prime(int(g_number.get())):
            g_number_error.config(text="G Number must be a prime number.")
        else:
            g_number_error.config(text="")
            valid += 1
    # ? Validate N
        if n_number.get() == "":
            n_number_error.config(text="N Number must not be empty.")
        elif not n_number.get().isdigit():
            n_number_error.config(text="N Number must be a prime number.")
        elif not is_prime(int(n_number.get())):
            n_number_error.config(text="N Number must be a prime number.")
        else:
            n_number_error.config(text="")
            valid += 1
    # ? Validate Alice number
        if alice_number.get() == "":
            alice_number_error.config(text="Alice's Number must not be empty.")
        elif not alice_number.get().isdigit():
            alice_number_error.config(
                text="Alice's Number must be a positive integer.")
        else:
            alice_number_error.config(text="")
            valid += 1
    # ? Validate Bob number
        if bob_number.get() == "":
            bob_number_error.config(text="Bob's Number must not be empty.")
        elif not bob_number.get().isdigit():
            bob_number_error.config(
                text="Bob's Number must be a positive integer.")
        else:
            bob_number_error.config(text="")
            valid += 1
        if valid == 4:
            alice_key.config(
                bg="white",
                relief="solid"
            )
            root.update()
            time.sleep(0.5)
            alice_key.config(text="A = g ** (alice number) mod n")
            root.update()
            time.sleep(0.5)
            new_value = alice_key.cget(
                "text") + f"\nA = {g_number.get()} ** {alice_number.get()} mod {n_number.get()}"
            alice_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            A_user_comput_value = step_one(int(g_number.get()), int(
                alice_number.get()), int(n_number.get()))
            new_value = alice_key.cget("text") + f"\nA = {A_user_comput_value}"
            alice_key.config(text=new_value)

            root.update()
            time.sleep(0.5)
            bob_key.config(
                bg="white",
                relief="solid"
            )
            root.update()
            time.sleep(0.5)
            bob_key.config(text="B = g ** (bob number) mod n")
            root.update()
            time.sleep(0.5)
            new_value = bob_key.cget(
                "text") + f"\nB = {g_number.get()} ** {bob_number.get()} mod {n_number.get()}"
            bob_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            B_user_comput_value = step_one(int(g_number.get()), int(
                bob_number.get()), int(n_number.get()))
            new_value = bob_key.cget("text") + f"\nB = {B_user_comput_value}"
            bob_key.config(text=new_value)

            root.update()
            time.sleep(0.5)
            new_value = alice_key.cget(
                "text") + f"\n\nKey from Alice = B ** (alice number) mod n"
            alice_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            new_value = alice_key.cget(
                "text") + f"\nKey from Alice = {B_user_comput_value} ** {alice_number.get()} mod {n_number.get()}"
            alice_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            A_key = step_two(B_user_comput_value, int(
                alice_number.get()), int(n_number.get()))
            new_value = alice_key.cget("text") + f"\nKey from Alice = {A_key}"
            alice_key.config(text=new_value)

            root.update()
            time.sleep(0.5)
            new_value = bob_key.cget(
                "text") + f"\n\nKey from Bob = B ** (bob number) mod n"
            bob_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            new_value = bob_key.cget(
                "text") + f"\nKey from Bob = {A_user_comput_value} ** {bob_number.get()} mod {n_number.get()}"
            bob_key.config(text=new_value)
            root.update()
            time.sleep(0.5)
            B_key = step_two(A_user_comput_value, int(
                bob_number.get()), int(n_number.get()))
            new_value = bob_key.cget("text") + f"\nKey from Bob = {B_key}"
            bob_key.config(text=new_value)
