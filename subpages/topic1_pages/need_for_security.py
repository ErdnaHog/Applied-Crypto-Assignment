from main import mainframe, font_family, main_colour, button_colour, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry, Tk
from subpages import clear_screen, get_Topic1


class Need_for_security:
    def need_for_security_page():
        clear_screen(mainframe)
        Topic1 = get_Topic1()
    # ? Title
        label = Label(
            mainframe,
            text="Topic 1: Need For Security",
            font=(font_family, 24),
            background="#ffffff")
        label.grid(row=0, column=0, columnspan=2, padx=1)
    # ? Content Frame
        content_frame = Frame(
            mainframe,
            bg=main_colour
        )
        content_frame.grid(row=1, column=0, columnspan=2)
        Label(
            content_frame,
            text="Need for Security.\nIn today’s world, we use the Internet for many purposes.\nWe use the Internet to email our friends or colleagues.\nWe use the Internet to WhatsApp our families and clients.\nWe also use the Internet to make purchases or for banking.\nIf we send confidential information in the clear, i.e. unprotected.\nThe confidential information is not secure and can be compromised.",
            font=(font_family, 14),
            bg="#ffffff"
        ).grid(row=0, column=0, padx=1, pady=50)
    # ? Button Frame
        button_frame = Frame(
            mainframe,
            bg=main_colour
        )
        button_frame.grid(row=2, column=0, columnspan=2)
        Button(
            button_frame,
            text="Next Content",
            font=h3_font,
            bg=button_colour,
            command=Topic1.trusted_system_page
        ).grid(row=0, column=1, padx=10)
