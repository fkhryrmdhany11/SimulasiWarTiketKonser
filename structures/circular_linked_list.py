# Circular linked list
# dipakai untuk rotasi rekomendasi konser
# (setiap menu utama dibukan rekomendasi berputar ke konser berikutnya secara terus menerus)

class CircularNode:
    def __init__(self, data):
        self.data = data # isi data node (string nama artis- genre)
        self.next = None # pointer ke node berikutnya

class CircularLinkedList:
    def __init__(self):
        self.head = None # node pertama (kosong)
        self.current = None # node yang sedang aktif (giliran tampil sekarang)

    def append(self, data):
        """
        - Menambahkan node baru di akhir list
        - Karena circular, jadi node terakhir selalu menunjuk ke head
        """
        new_node = CircularNode(data)

        # jika list kosong, maka node baru menunjuk ke dirinya sendiri
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.current = self.head # current dimulai dari head
            return

        # cari node terakhir
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node # sambungkan node terakhir ke node baru
        new_node.next = self.head # node baru menunjuk ke head

    def next_promo(self):
        if self.current is None: # kembalikan none jika list kosong
            return None

        data = self.current.data # ambil data dari node sekarang
        self.current = self.current.next # geser ke node berikutnya (rotasi)
        return data