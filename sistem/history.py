# sistem history (menampilkan riwayat transaksi)

from utils.util import print_header, cls

class History_Sistem:
    def __init__(self, system):
        self.system = system

    def tampilkan_history(self):
        """
        - Menampilkan semua transaksi dari DLL
        - Traversal dilakukan dari head (transaksi terlama) ke tail (transaksi terbaru)
        """
        cls()
        print_header("HISTORY")

        # mulai dari head (node pertama/transaksi terlama)
        current = self.system.user_login.history.head
        if not current:
            print("Belum ada transaksi.")
            return

        # telusuri setiap node sampai akhir list
        while current:
            transaksi = current.data # ambil dict transaksi dari node
            print(f"Artis    : {transaksi['artis']}")
            print(f"Genre    : {transaksi['genre']}")
            print(f"Seat     : {transaksi['seat']}")
            print(f"Kategori : {transaksi['kategori']}")
            print(f"Harga    : Rp{transaksi['harga']:,}")
            print(f"Waktu    : {transaksi['waktu']}")
            print(f"Status   : {transaksi['status']}")
            print("-" * 60)
            current = current.next # pindah ke node berikutnya

    def searching_history(self):
        cls()
        print_header("PENCARIAN")
        keyword = str(input("Masukkan Nama Artis: "))

        # mulai pencarian dari node pertama histori
        current = self.system.user_login.history.head
        ditemukan = False

        print()
        print_header("HASIL PENCARIAN")
        while current:
            transaksi = current.data
            if keyword in transaksi["artis"].lower():
                ditemukan = True
                print(f"Artis    : {transaksi['artis']}")
                print(f"Genre    : {transaksi['genre']}")
                print(f"Seat     : {transaksi['seat']}")
                print(f"Kategori : {transaksi['kategori']}")
                print(f"Harga    : Rp{transaksi['harga']:,}")
                print(f"Waktu    : {transaksi['waktu']}")
                print(f"Status   : {transaksi['status']}")
                print("-" * 60)
            current = current.next

        if not ditemukan:
            print("History tidak ditemukan.")