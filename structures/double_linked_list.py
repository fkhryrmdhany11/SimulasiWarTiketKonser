# Double Linked List
# dipakai untuk menyimpan semua history transaksi
# (menyimpan semua riwayat booking user secara berurutan)
# Setiap node punya pointer ke node sebelumnya dan sesudahnya, sehingga bisa dibaca dua arah

class DoubleNode:
    def __init__(self, data):
        self.data = data # isi data node (berupa dict transaksi)
        self.next = None # pointer ke node berikutnya
        self.prev = None # pointer ke node sebelumnya


class DoubleLinkedList:
    def __init__(self):
        self.head = None # node pertama (paling awal) = kosong
        self.tail = None # node terakhir (paling baru) = kosong

    # TAMBAH HISTORY (di akhir list)
    def append(self, data):
        new_node = DoubleNode(data)
        
        # jika list kosong, maka node baru jadi head sekaligus tail
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            return

        # sambungkan tail lama ke node baru
        self.tail.next = new_node # tail lama menunjuk ke node baru
        new_node.prev = self.tail # node baru menunjuk balik ke tail lama
        self.tail = new_node # sekarang node baru jadi tail baru

    # TAMPIL HISTORY (menampilkan semua data dengan urutan data lama ke baru)
    def tampilkan(self):
        current = self.head

        # jika data kosong, cetak pesan
        if current is None:
            print("History kosong")
            return

        # traversal dari head ke tail menggunakan pointer next
        while current:
            print(current.data)
            current = current.next