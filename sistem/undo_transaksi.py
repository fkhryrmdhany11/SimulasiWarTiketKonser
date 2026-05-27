class UndoTransaksi_Sistem:

    def __init__(self, system):
        self.system = system

    # =========================
    # UNDO TRANSAKSI
    # =========================
    def undo_transaksi(self):
        # ambil transaksi terakhir
        transaksi = self.system.user_login.undo_stack.pop()
        if not transaksi:
            print("\nTidak ada transaksi untuk diundo.")
            return

        artis = transaksi["artis"]
        seat = transaksi["seat"]

        # =========================
        # KOSONGKAN SEAT
        # =========================
        for konser in self.system.konser_list:

            if konser["artis"] == artis:
                seats = konser["seats"]
                seats[seat]["booked"] = False
                seats[seat]["username"] = None
                break

        # =========================
        # UPDATE STATUS HISTORY
        # =========================
        current = self.system.user_login.history.head
        while current:
            data = current.data
            if (data["artis"] == artis and data["seat"] == seat and data["status"] == "AKTIF"):
                data["status"] = "DIBATALKAN"
                break
            current = current.next

        # save
        self.system.save_data()
        self.system.save_konser()

        print("\nTransaksi berhasil dibatalkan.")