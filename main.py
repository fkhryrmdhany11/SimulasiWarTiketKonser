from system.sistem import SistemWarTiket
from utils.util import print_header, cls, pembatas
from menu.menu import menu_awal, menu_utama
sistem = SistemWarTiket()

while True:
    print_header("SISTEM WAR TIKET KONSER")
    print("1. Masuk")
    print("0. Keluar")
    pembatas()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        verif = menu_awal(sistem)
        if verif and sistem.user_login:
            menu_utama(sistem)
        cls()
    elif pilihan == "0":
        print("Terima kasih sudah menggunakan sistem.")
        break
    else:
        print("Menu tidak valid.")