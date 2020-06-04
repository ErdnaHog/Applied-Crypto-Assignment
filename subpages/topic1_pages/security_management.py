from main import mainframe, font_family, main_colour, button_colour, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry, Tk
from subpages import clear_screen


class Security_management:
    def security_management_page():
        clear_screen(mainframe)
    # ? Title
        label = Label(
            mainframe,
            text="Topic 1.3: Security Management Practices",
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
            text="There are 4 key characteristics of a good security policy:\nAffordability: the security policy should not be too costly and incur too much effort to implement\nFunctionality: there should be available security mechanism to support the security policy\nCultural issues: the security policy should gel with people’s expectations, working style and beliefs\n Legality: the policy should meet legal requirements.",
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
            text="Previous Content",
            font=h3_font,
            bg=button_colour
        ).grid(row=0, column=0, padx=10)
        Button(
            button_frame,
            text="Next Content",
            font=h3_font,
            bg=button_colour
        ).grid(row=0, column=1, padx=10)
