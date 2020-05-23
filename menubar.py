from main import root
from tkinter import Menu
from subpages.topic2 import Topic2
from subpages.topic3 import Topic3

menubar = Menu(root)

topic1 = Menu(menubar, tearoff=0)
topic1.add_command(label='Learn')
topic1.add_command(label='Quiz')

menubar.add_cascade(label='Need For Information Security', menu=topic1)

topic2 = Menu(menubar, tearoff=0)
topic2.add_command(label='Shift cipher', command=Topic2.shift_cipher_page)
topic2.add_command(label='Mono-alphabet cipher',
                   command=Topic2.mono_alphabet_cipher_page)
topic2.add_command(label='Rail fence technique', command=Topic2.rail_fence_cipher_page)
topic2.add_command(label='Simple columnar transposition technique')
topic2.add_command(label='Vernam cipher')

menubar.add_cascade(label='Cryptography Concepts and Technqiues', menu=topic2)

topic3 = Menu(menubar, tearoff=0)
topic3.add_command(label="AES", command=Topic3.aes_page)
menubar.add_cascade(label='Symmetric Algorithms', menu=topic3)
