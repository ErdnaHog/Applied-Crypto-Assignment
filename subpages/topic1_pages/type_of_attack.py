from main import mainframe, font_family, main_colour, button_colour, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry, Tk
from subpages import clear_screen


class Type_of_attack:
    def type_of_attack_page():
        clear_screen(mainframe)
    # ? Title
        label = Label(
            mainframe,
            text="Topic 1.4: Types of Attack",
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
            text="Attacks can be classified as passive attacks or active attacks\nA passive attack does not involve any modifications to the contents of an original message typically involves eavesdropping or monitoring of data transmission compromises data confidentiality.\nAn active attack involves modification to the contents of the original message.\nThere are 3 sub-categories of active attacks:\n- Interruption attack affects the availability of information/system\n- Modification attack affects the integrity of a message\n- Fabrication attack affects the authenticity of the communication.",
            font=(font_family, 14),
            bg="#ffffff",
            wraplength=800
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
