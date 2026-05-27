class History_Sistem:
    def __init__(self, system):
            self.system = system

    def tampilkan_history(self):
        print("=" * 50)
        print("         HISTORY TRANSAKSI")
        print("=" * 50)

        current = self.system.user_login.history.head

        if not current:
            print("Belum ada transaksi.")
            return

        while current:
            transaksi = current.data
            print(f"Artis    : {transaksi['artis']}")
            print(f"Genre    : {transaksi['genre']}")
            print(f"Seat     : {transaksi['seat']}")
            print(f"Kategori : {transaksi['kategori']}")
            print(f"Harga    : Rp{transaksi['harga']}")
            print(f"Waktu    : {transaksi['waktu']}")
            print(f"Status   : {transaksi['status']}")
            print("-" * 50)

            current = current.next