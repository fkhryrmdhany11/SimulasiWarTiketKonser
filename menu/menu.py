from utils.util import print_header, cls, pembatas, verif
from system.daftar_konser import cari_konser, tampilkan_konser
from system.booking import booking_tiket
from system.sistem import SistemWarTiket
sistem = SistemWarTiket()

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
            sistem.register()
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

def menu_utama(sistem):
    cls()
    while sistem.user_login:
        print_header("MENU UTAMA")
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
            menu_booking_seat()
            cls()

        elif pilihan == "3":
            menu_histori_transaksi()
            cls()

        elif pilihan == "4":
            menu_batalkan_transaksi()
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
        print("1. Rekomendasi Konser")
        print("2. Searching Konser")
        print("3. Tampilkan Konser")
        print("0. Keluar")
        pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            pass

        elif pilihan == "2":
            cari_konser()
            verif()

        elif pilihan == "3":
            tampilkan_konser()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_booking_seat():
    cls()
    while True:
        print_header("BOOKING SEAT")
        print("1. Booking Seat")
        print("2. Searching Konser")
        print("3. Tampilkan Konser")
        print("0. Keluar")
        pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            pass
            verif()

        elif pilihan == "2":
            cari_konser()
            verif()

        elif pilihan == "3":
            tampilkan_konser()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_batalkan_transaksi():
    cls()
    while True:
        print_header("BATALKAN TRANSAKSI")
        print("1. Batalkan Transaksi")
        print("2. Searching Transaksi")
        print("3. Tampilkan Transaksi")
        print("0. Keluar")
        pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            pass
            verif()

        elif pilihan == "2":
            cari_konser()
            verif()

        elif pilihan == "3":
            tampilkan_konser()
            verif()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            verif()

def menu_histori_transaksi():
    cls()
    while True:
        print_header("HISTORI TRANSAKSI")
        print("1. Searching Histori")
        print("2. Tampilkan Histori")
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