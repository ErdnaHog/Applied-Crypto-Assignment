from main import root
from tkinter import *


def clear_screen(root):
    _list = root.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    for item in _list:
        item.grid_forget()

