class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # TAMBAH HISTORY
    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # TAMPIL HISTORY
    def tampilkan(self):
        current = self.head
        if current is None:
            print("History kosong")
            return

        while current:
            print(current.data)
            current = current.next