from tkinter import *

root = Tk()

root.geometry("800x400")

root.title("Crypto")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# mainframe.grid(pady=100, padx=100)


def return_menu():
    from menubar import menubar
    return menubar


root.config(menu=return_menu())
