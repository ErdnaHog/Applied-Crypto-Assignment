from main import mainframe, font_family, main_colour, button_colour, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry, Tk
from subpages import clear_screen


class Security_model:
    def security_model_page():
        clear_screen(mainframe)
    # ? Title
        label = Label(
            mainframe,
            text="Topic 1.2: Security Model",
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
            text="There are 4 approaches to implement a security model.\n-No Security: We do not need to use additional security protection.\n-Security through obscurity: We secure confidential information by hiding them\n-host security: We provide security by protecting the host\n-network security: We protect the network",
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
