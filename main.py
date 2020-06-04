from tkinter import *
import os

# * Global Variable
font_family = "Courier"
my_file_path = os.path.abspath(os.path.dirname(__file__))
main_colour = "#63ace5"
button_colour = "#e7eff6"
button_colour2 = "#4b86b4"
# * fonts
h1_font = (font_family, 20)
h2_font = (font_family, 14)
h3_font = (font_family, 12)
error_font = (font_family, 14)
# * box width
box_width = 35

root = Tk()

root.geometry("1400x700")

root.title("Crypto")

mainframe = Frame(root, width=1100, height=500, bg=main_colour)
mainframe.grid(column=0, row=0)
# mainframe.grid(pady=100, padx=100)

main_page = Frame(mainframe, bg="#4b86b4")
main_page.grid(row=0, column=0)
Label(main_page, text="Welcome to Crypto Learning Page",
      font=("Courier", 40), background="#ffffff").grid(row=0, column=0, padx=1, pady=50)


def return_menu():
    from menubar import menubar
    return menubar


root.config(menu=return_menu(), background=main_colour)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
