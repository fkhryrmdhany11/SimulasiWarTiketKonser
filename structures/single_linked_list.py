# Single linked list -> diimplementasikan sebagai stack
# dipakai untuk fitur undo transaksi (menyimpan transaksi agar bisa dibatalkan)

class SingleNode:
    def __init__(self, data):
        self.data = data # isi data node (berupa dict transaksi)
        self.next = None # pointer ke node berikutnnya 


class SingleLinkedList:
    """
    - Single linked list yang digunakan sebagai stack
    - top selalu menunjuk ke node paling atas (yang terakhir di tambahkan)
    """

    def __init__(self):
        self.top = None 

    # PUSH (menambahkan data ke atas stack)
    def push(self, data):
        new_node = SingleNode(data)
        new_node.next = self.top # node baru menumpuk di atas top lama
        self.top = new_node # top sekarang adalah new_node

    # POP (mengambil dan menghapus data dari atas stack)
    def pop(self):
        if self.top is None: # jika stack kosong, kembalikan None
            return None 

        data = self.top.data # simpan data dari top
        self.top = self.top.next # geser top ke node berikutnya
        return data # kembalikan data yang di pop

    # CEK KOSONG
    def is_empty(self):
        return self.top is None