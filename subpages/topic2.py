from main import root
from subpages.topic2_pages.shift_cipher import Shift_cipher
from subpages.topic2_pages.mono_alphabet_cipher import Mono_alphabet_cipher
from subpages.topic2_pages.rail_fence_cipher import Rail_fence_cipher
from subpages.topic2_pages.vernam_cipher import Vernam_cipher
from subpages.topic2_pages.simple_columnar_transposition import Simple_columnar_transposition


class Topic2(Shift_cipher, Mono_alphabet_cipher, Rail_fence_cipher, Vernam_cipher, Simple_columnar_transposition):
    def clear_inputs(key, plaintext, ciphertext):
        key.delete(0, 100)
        plaintext.delete("1.0", "end")
        ciphertext.delete("1.0", "end")

        if root.grid_slaves(3, 1):
            root.grid_slaves(3, 1)[0].grid_forget()
        if root.grid_slaves(4, 1):
            root.grid_slaves(4, 1)[0].grid_forget()
