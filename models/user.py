from structures.double_linked_list import DoubleLinkedList
from structures.single_linked_list import SingleLinkedList

# =========================
# CLASS USER
# =========================

class User:
    def __init__(self, username, password):

        self.username = username
        self.password = password

        # history transaksi
        self.history = DoubleLinkedList()

        # undo transaksi
        self.undo_stack = SingleLinkedList()