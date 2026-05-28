class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.top = None

    # PUSH
    def push(self, data):
        new_node = SingleNode(data)
        new_node.next = self.top
        self.top = new_node

    # POP
    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    # CEK KOSONG
    def is_empty(self):
        return self.top is None