from main import mainframe, font_family, main_colour, button_colour, h1_font, h2_font, h3_font, box_width
from tkinter import Label, Text, Button, Message, Frame, StringVar, Entry, Tk
from subpages import clear_screen, get_Topic1


class Trusted_system:
    def trusted_system_page():
        clear_screen(mainframe)
        Topic1 = get_Topic1()
    # ? Title
        label = Label(
            mainframe,
            text="Topic 1.1: Trusted System and Reference Monitor",
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
            text="What is a trusted system?\nA trusted system is a computer system that can be trusted to a specified extent.\nIt is able to enforce a specified security policy",
            font=(font_family, 14),
            bg="#ffffff"
        ).grid(row=0, column=0, padx=1, pady=(50, 0))
        Label(
            content_frame,
            text="Reference Monitor: A trusted system can be implemented using a reference monitor.\nWhat is a reference monitor? A reference monitor is an entity at the heart of a computer system.\nIt is responsible for all decisions related to enforcing access controls.\nSuppose a subject would like to request for an action on an object,\nThe reference monitor will check the request to determine if the subject has the privilege to do so.\nIf he has, access is granted. If not, access is denied.\nFor example, if a user requests to read a file,\nThe reference monitor will check if the user has read access to the file.\nIf he has, access is granted. If not, access is denied.",
            font=(font_family, 14),
            bg="#ffffff"
        ).grid(row=1, column=0, padx=1, pady=50)
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
            bg=button_colour,
            command=Topic1.need_for_security_page
        ).grid(row=0, column=0, padx=10)
        Button(
            button_frame,
            text="Next Content",
            font=h3_font,
            bg=button_colour,
            command=Topic1.security_model_page
        ).grid(row=0, column=1, padx=10)
