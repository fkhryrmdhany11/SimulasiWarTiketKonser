# booking.py 
# dipakai untuk menangani seluruh proses pemesanan tiket konser

from datetime import datetime
from utils.util import print_header, cls, print_section

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
        cls()
        print_header("STAGE")
        print_section("VIP SECTION")
        vip_count = 0
        for kode, data in seats.items():
            if data["kategori"] == "VIP":
                # menampilkan status seat:
                # [ ] = tersedia
                # [x] = sudah dibooking
                status = "[X]" if data["booked"] else "[ ]"
                print(f"{kode} {status}", end="   ")
                vip_count += 1
                # buat tampilan 5 seat per baris
                if vip_count % 5 == 0:
                    print()

        print_section("REGULAR SECTION")
        reg_count = 0
        for kode, data in seats.items():
            if data["kategori"] == "REGULER":
                status = "[X]" if data["booked"] else "[ ]"
                print(f"{kode} {status}", end="   ")
                reg_count += 1
                # 5 seat per baris
                if reg_count % 5 == 0:
                    print()

        print("\n" + "=" * 60)
        print("[ ] = TERSEDIA")
        print("[X] = TERBOOKING")
        print("=" * 60)

    # =========================
    # BOOKING SEAT
    # =========================
    def booking_seat(self, konser_list, username,):
        # ================= CARI ARTIS =================
        cls()
        print_header("PENCARIAN")
        keyword = str(input("Masukkan Nama Artis: "))
        hasil = self.cari_konser(konser_list,keyword)

        # jika konser tidak ditemukan
        if not hasil:
            print("\nKonser tidak ditemukan.")
            return

        # ================= TAMPILKAN HASIL =================
        print()
        print_header("HASIL PENCARIAN")
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

        # jika seat tidak ditemukan
        if seat not in seats:
            print("\nSeat tidak ditemukan.")
            return

        # jika seat sudah dibooking
        if seats[seat]["booked"]:
            print("\nSeat sudah dibooking.")
            return

        # ================= BOOKING =================
        seats[seat]["booked"] = True # ubah status seat menjadi sudah terbooking
        seats[seat]["username"] = username # simpan informasi user
        self.sistem.save_konser()

        # ================= TRANSAKSI =================
        # simpan detail transaksi sebagai riwayat pemesanan
        transaksi = {"artis": konser["artis"],
                     "genre": konser["genre"],
                     "seat": seat,
                     "kategori": seats[seat]["kategori"],
                     "harga": seats[seat]["harga"],
                     "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                     "status": "AKTIF"}

        # simpan transaksi ke DLL sebagai history
        self.sistem.user_login.history.append(transaksi)

        # simpan transaksi ke Stack (SLL) untuk fitur undo
        self.sistem.user_login.undo_stack.push(transaksi)
        self.sistem.save_data()
        self.sistem.save_konser()

        # ================= OUTPUT =================
        cls()
        print_header("BOOKING BERHASIL")

        print(f"Username : {username}")
        print(f"Artis    : {konser['artis']}")
        print(f"Genre    : {konser['genre']}")
        print(f"Seat     : {seat}")
        print(f"Kategori : {seats[seat]['kategori']}")
        print(f"Harga    : Rp{seats[seat]['harga']:,}")
        print(f"Waktu    : {transaksi['waktu']}")
        print("=" * 60)

    # =========================
    # JALANKAN BOOKING sistem 
    # =========================
    def jalankan_booking_sistem(self):
        # jalankan fitur booking menggunakan data user yang sedang login 
        self.booking_seat(self.sistem.konser_list, self.sistem.user_login.username)