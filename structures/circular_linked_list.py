class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.current = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def next_promo(self):
        if self.current is None:
            return None

        data = self.current.data
        self.current = self.current.next
        return data