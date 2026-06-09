from utils.util import print_header, cls, pembatas, verif
from sistem.daftar_konser import cari_konser, tampilkan_konser
from sistem.booking import Booking_Sistem
from sistem.rekomendasi import Rekomendasi_Sistem
from sistem.undo_transaksi import UndoTransaksi_Sistem
from sistem.history import History_Sistem


def menu_awal(sistem):
    cls()
    while True:
        print_header("SISTEM WAR TIKET KONSER")
        print("1. Register")
        print("2. Login")
        print("0. Kembali")
        pembatas()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            user = sistem.register()
            if user:
                menu_genre(user)
                sistem.save_data()
            tanya = input("Lanjut login sekarang? (y/n): ").lower()
            if tanya == "y" and sistem.login():
                return True
            verif()

        elif pilihan == "2":
            if sistem.login():
                return True
            verif()

        elif pilihan == "0":
            return False

        else:
            print("Menu tidak valid.")
            verif()

def menu_genre(user):
    cls()
    while True:
        print_header("GENRE YANG DISUKAI")
        print("1. INDIE")
        print("2. K-POP")
        print("3. HIP HOP")
        print("4. EDM")
        print("5. COUNTRY")
        print("6. DANGDUT")
        print("7. POP")
        print("8. R&B")
        print("9. ROCK")
        pembatas()
        pilihan = input("Pilih Genre: ")

        genre_map = {
            "1": "INDIE",
            "2": "K-POP",
            "3": "HIP HOP",
            "4": "EDM",
            "5": "COUNTRY",
            "6": "DANGDUT",
            "7": "POP",
            "8": "R&B",
            "9": "ROCK"
        }

        if pilihan in genre_map:
            genre = genre_map[pilihan]
            user.minat_genre = genre
            verif()
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_utama(sistem):
    cls()
    rekomendasi_sistem = Rekomendasi_Sistem(sistem)
    while sistem.user_login:
        print_header("MENU UTAMA")
        rekomendasi_sistem.tampilkan_rekomendasi()
        pembatas()
        print("1. Daftar Konser")
        print("2. Booking Seat")
        print("3. Histori Transaksi")
        print("4. Batalkan Transaksi")
        print("0. Keluar")
        pembatas()
        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            menu_daftar_konser()
            cls()

        elif pilihan == "2":
            menu_booking_seat(sistem)
            cls()

        elif pilihan == "3":
            menu_histori_transaksi(sistem)
            cls()

        elif pilihan == "4":
            menu_batalkan_transaksi(sistem)
            cls()
        
        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_daftar_konser():
    cls()
    while True:
        print_header("DAFTAR KONSER")
        print("1. Cari Konser")
        print("2. Tampilkan Daftar Konser")
        print("0. Keluar")
        pembatas()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            cari_konser()
            verif()

        elif pilihan == "2":
            tampilkan_konser()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_booking_seat(sistem):
    cls()
    booking_tiket = Booking_Sistem(sistem)
    while True:
        print_header("BOOKING SEAT")
        print("1. Booking Seat")
        print("0. Keluar")
        pembatas()
        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            booking_tiket.jalankan_booking_sistem()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_batalkan_transaksi(sistem):
    cls()
    undo_sistem = UndoTransaksi_Sistem(sistem)
    while True:
        print_header("BATALKAN TRANSAKSI")
        print("1. Batalkan Transaksi")
        print("0. Keluar")
        pembatas()
        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            undo_sistem.undo_transaksi()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_histori_transaksi(sistem):
    cls()
    history_sistem = History_Sistem(sistem)
    while True:
        print_header("HISTORI TRANSAKSI")
        print("1. Searching Histori")
        print("2. Tampilkan Histori")
        print("0. Keluar")
        pembatas()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            history_sistem.searching_history()
            verif()

        elif pilihan == "2":
            history_sistem.tampilkan_history()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()