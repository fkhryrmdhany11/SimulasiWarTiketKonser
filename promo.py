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

    def hapus_promo(self, nama):
        '''hapus promo konser tertentu dari daftar'''
        if self.head is None:
            print('Daftar promo kosong')
            return
        
        temp = self.head
        prev = None
        
        if temp.data['nama'] == nama:
            # cari node terakhir 
            last = self.head
            while last.next != self.head:
                last = last.next

            if self.head == self.head.next:
                self.head = None
                self.current = None
            else:
                self.head = self.head.next
                last.next = self.head
                if self.current == temp:
                    self.current = self.head
            return
        
        # jika node ditengah / akhir
        while temp != self.head:
            prev = temp
            temp = temp.next
            if temp.data['artis'] == nama:
                prev.next = temp.next
                if self.current == temp:
                    self.current = prev.next
                return
        
        print(f'Promo "{nama}" tidak ditemukan ')

    def tampilkan_promo(self):
        '''menampilkan promo berputar'''
        if not self.current:
            print('Promo tidak tersedia')
            return
        
        while True:
            print('\n=== PROMO HARI INI ===')
            print(self.current.data)
            print('-'* 30)
            
            self.current = self.current.next # pindah ke promo berikutnya
            
            time.sleep(0.5)
            stop = input('ketik "s" untuk berhenti: ')
            if stop.lower() == 's':
                break


#tes
promo = CircularPromo()

promo.tambah_promo('NCT Dream - The Dream Show 6')
promo.tambah_promo('NIKI Buzz Tour')
promo.tambah_promo('NCT 127 World tour')
promo.tambah_promo('Mark Lee The First Fruit Tour')

promo.tampilkan_promo()