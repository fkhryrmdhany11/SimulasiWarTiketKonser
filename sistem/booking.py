from datetime import datetime

class Booking_Sistem:

    def __init__(self, sistem):
        self.sistem = sistem

    # =========================
    # CARI KONSER BERDASARKAN ARTIS
    # =========================
    def cari_konser(self, konser_list, keyword):
        hasil = []
        for konser in konser_list:
            if keyword.lower() in konser["artis"].lower():
                hasil.append(konser)
        return hasil

    # =========================
    # TAMPILKAN LAYOUT VENUE
    # =========================
    def tampilkan_layout_venue(self, seats):
        print("=" * 55)
        print(" " * 24 + "STAGE")
        print("=" * 55)

        # ================= VIP =================
        print("\n---------------- VIP SECTION ----------------\n")

        vip_count = 0
        for kode, data in seats.items():
            if data["kategori"] == "VIP":
                status = "[X]" if data["booked"] else "[ ]"
                print(f"{kode} {status}", end="   ")
                vip_count += 1
                # 5 seat per baris
                if vip_count % 5 == 0:
                    print()

        # ================= REGULER =================
        print("\n\n------------- REGULAR SECTION --------------\n")

        reg_count = 0
        for kode, data in seats.items():
            if data["kategori"] == "REGULER":
                status = "[X]" if data["booked"] else "[ ]"
                print(f"{kode} {status}", end="   ")
                reg_count += 1
                # 5 seat per baris
                if reg_count % 5 == 0:
                    print()

        print("\n\n" + "=" * 55)
        print("[ ] = TERSEDIA")
        print("[X] = TERBOOKING")
        print("=" * 55)

    # =========================
    # BOOKING SEAT
    # =========================
    def booking_seat(self, konser_list, username,):
        # ================= CARI ARTIS =================
        keyword = input("Cari artis: ")
        hasil = self.cari_konser(konser_list,keyword)

        # konser tidak ditemukan
        if not hasil:
            print("\nKonser tidak ditemukan.")
            return

        # ================= TAMPILKAN HASIL =================
        print("\nHASIL PENCARIAN\n")

        for i, konser in enumerate(hasil, start=1):
            print(f"{i}. {konser['artis']} ({konser['genre']})")

        # ================= PILIH KONSER =================
        try:
            pilihan = int(input("\nPilih konser: ")) - 1
            konser = hasil[pilihan]
        except:
            print("\nPilihan tidak valid.")
            return

        # ================= AMBIL SEAT =================
        seats = konser["seats"]
        # ================= TAMPILKAN VENUE =================
        self.tampilkan_layout_venue(seats)
        # ================= INPUT SEAT =================
        seat = input("\nPilih seat: ").upper()

        # seat tidak ditemukan
        if seat not in seats:
            print("\nSeat tidak ditemukan.")
            return

        # seat sudah dibooking
        if seats[seat]["booked"]:
            print("\nSeat sudah dibooking.")
            return

        # ================= BOOKING =================
        seats[seat]["booked"] = True
        seats[seat]["username"] = username
        self.sistem.save_konser()

        # ================= TRANSAKSI =================
        transaksi = {"artis": konser["artis"],
                     "genre": konser["genre"],
                     "seat": seat,
                     "kategori": seats[seat]["kategori"],
                     "harga": seats[seat]["harga"],
                     "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                     "status": "AKTIF"}

        # simpan transaksi
        self.sistem.user_login.history.append(transaksi)
        self.sistem.user_login.undo_stack.push(transaksi)
        self.sistem.save_data()
        self.sistem.save_konser()

        # ================= OUTPUT =================
        print("\n" + "=" * 45)
        print("         BOOKING BERHASIL")
        print("=" * 45)

        print(f"Username : {username}")
        print(f"Artis    : {konser['artis']}")
        print(f"Genre    : {konser['genre']}")
        print(f"Seat     : {seat}")
        print(f"Kategori : {seats[seat]['kategori']}")
        print(f"Harga    : Rp{seats[seat]['harga']}")
        print(f"Waktu    : {transaksi['waktu']}")
        print("=" * 45)

    # =========================
    # TAMPILKAN HISTORY
    # =========================
    def tampilkan_history(self):
        print("=" * 50)
        print("         HISTORY TRANSAKSI")
        print("=" * 50)

        current = self.sistem.user_login.history.head
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

    # =========================
    # JALANKAN BOOKING sistem
    # =========================
    def jalankan_booking_sistem(self):
        self.booking_seat(self.sistem.konser_list, self.sistem.user_login.username)