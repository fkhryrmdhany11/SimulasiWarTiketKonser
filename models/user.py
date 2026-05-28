# menyimpan data user
from structures.double_linked_list import DoubleLinkedList
from structures.single_linked_list import SingleLinkedList

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # doubly linked list
        self.history = DoubleLinkedList()
        # singly linked list
        self.undo_stack = SingleLinkedList()
        # minat genre
        self.minat_genre = ""   # menyimpan genre favorit user untuk rekomendasi konser