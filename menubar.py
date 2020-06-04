from subpages.topic3 import Topic3
from subpages.topic2 import Topic2
from subpages.topic1 import Topic1
from tkinter import Menu
from main import root

menubar = Menu(root)

topic1 = Menu(menubar, tearoff=0)

topic1_sub_menu = Menu(topic1, tearoff=0)
topic1_sub_menu.add_command(
    label="Need for security", command=Topic1.need_for_security_page)
topic1_sub_menu.add_command(
    label="Trusted systems and reference monitor", command=Topic1.trusted_system_page)
topic1_sub_menu.add_command(
    label="Security models", command=Topic1.security_model_page)
topic1_sub_menu.add_command(
    label="Security management practices", command=Topic1.security_management_page)
topic1_sub_menu.add_command(
    label="Types of attacks", command =Topic1.type_of_attack_page)

topic1.add_cascade(label='Learn', menu=topic1_sub_menu)
topic1.add_command(label='Quiz', command=Topic1.quiz_page)

menubar.add_cascade(label='Need For Information Security', menu=topic1)

topic2 = Menu(menubar, tearoff=0)
topic2.add_command(label='Shift cipher', command=Topic2.shift_cipher_page)
topic2.add_command(label='Mono-alphabet cipher',
                   command=Topic2.mono_alphabet_cipher_page)
topic2.add_command(label='Rail fence technique',
                   command=Topic2.rail_fence_cipher_page)
topic2.add_command(label='Simple columnar transposition technique',
                   command=Topic2.simple_columnar_transposition_page)
topic2.add_command(label='Vernam cipher', command=Topic2.vernam_cipher_page)
topic2.add_command(label='Diffie-Hellman Key Exchange',
                   command=Topic2.diffie_hellman_page)

menubar.add_cascade(label='Cryptography Concepts and Technqiues', menu=topic2)

topic3 = Menu(menubar, tearoff=0)
topic3.add_command(label="AES", command=Topic3.aes_page)
menubar.add_cascade(label='Symmetric Algorithms', menu=topic3)
