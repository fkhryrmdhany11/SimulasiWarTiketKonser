import util as ut
from settings import SistemWarTiket
sistem = SistemWarTiket()

def menu_awal(sistem):
    ut.cls()
    while True:
        ut.print_header("SISTEM WAR TIKET KONSER")
        print("1. Register")
        print("2. Login")
        print("0. Kembali")
        ut.pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            sistem.register()
            tanya = input("Lanjut login sekarang? (y/n): ").lower()
            if tanya == "y" and sistem.login():
                return True
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

        elif pilihan == "2":
            if sistem.login():
                return True
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

        elif pilihan == "0":
            return False

        else:
            print("Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

def menu_utama(sistem):
    ut.cls()
    while sistem.user_login:
        ut.print_header("SISTEM WAR TIKET KONSER")
        print("1. Daftar Konser")
        print("2. Booking Seat")
        print("3. Histori Transaksi")
        print("4. Batalkan Transaksi")
        print("0. Keluar")
        ut.pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            pass

        elif pilihan == "2":
            pass

        elif pilihan == "3":
            pass

        elif pilihan == "4":
            pass
        
        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            ut.cls()