import time 

class NodePromo:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularPromo:
    def __init__(self):
        # inisialisasi linked list kosong dengan pointer head merujuk ke none
        self.head = None
        self.current = None # pointer untuk rotasi

        self.tambah_promo({
            "artis": "NCT Dream",
            "diskon": "20%"
        })

        self.tambah_promo({
            "artis": "SEVENTEEN",
            "diskon": "15%"
        })

        self.tambah_promo({
            "artis": "AESPA",
            "diskon": "Buy 1 Get 1"
        })

    def tambah_promo(self, data):
        '''menambah node baru(promo baru) dengan data ke akhir linked list'''
        new_node = NodePromo(data)
        
        # jika list kosong, maka jadikan node baru sebagai head
        if self.head is None:
            self.head = new_node
            new_node.next = self.head # node baru menunjuk kembali ke head
            self.current = self.head # menyimpan posisi promo yang sedang ditampilkan
            return
        else:
            temp = self.head
            # loop sampai ketemu node terakhir
            while temp.next != self.head:
                temp = temp.next 
            temp.next = new_node # node terakhir menunjuk ke node baru
            new_node.next = self.head # node baru menunjuk kembali ke head


    def tampilkan_promo(self):
        '''menampilkan promo berputar'''
        if self.head is None:
            print('Promo tidak tersedia')
            return
        
        # tampilkan promo saat ini
        print('\n=== PROMO HARI INI ===')
        print(f"Konser : {self.current.data['artis']}")
        print(f"Diskon : {self.current.data['diskon']}")        
        print('-'* 30)
        
        self.current = self.current.next # pindah ke promo berikutnya