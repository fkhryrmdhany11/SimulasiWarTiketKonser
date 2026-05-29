# user.py 
# modul untuk menyimpan data user
from structures.double_linked_list import DoubleLinkedList
from structures.single_linked_list import SingleLinkedList

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # doubly linked list untuk menyimpan semua riwayat transaksi
        # dipilih karena dapat ditelusuri dua arah
        self.history = DoubleLinkedList()

        # singly linked list sebagai Stack untuk fitur undo (batalkan transaksi)
        # dipilih karena stack menerapkan prinsip LIFO
        self.undo_stack = SingleLinkedList()
        
        # minat genre
        self.minat_genre = ""   # menyimpan genre favorit user untuk rekomendasi konser