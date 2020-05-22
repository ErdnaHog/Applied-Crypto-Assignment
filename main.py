from tkinter import *

root = Tk()

root.geometry("800x400")

root.title("Crypto")


def return_menu():
    from menubar import menubar
    return menubar


root.config(menu=return_menu())
