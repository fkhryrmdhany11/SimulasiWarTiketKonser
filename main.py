from sistem.sistem import SistemWarTiket
from utils.util import print_header, cls, pembatas
from menu.menu import menu_awal, menu_utama

# membuat satu objek (sistem) yang akan dipakai sepanjang program berjalan
# di dalam __init__ nya sistem otomatis load data user dan data konser dari json
sistem = SistemWarTiket()

#loop utama program 
while True:
    print_header("SISTEM WAR TIKET KONSER")
    print("1. Masuk")
    print("0. Keluar")
    pembatas()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # jalankan menu awal (regis/login)
        # fungsi menu_awal() mengembalikan true jika login berhasil
        verif = menu_awal(sistem)

        # jika login berhasil dan ada user yang sedang login:
        if verif and sistem.user_login:
            menu_utama(sistem) # masuk ke menu utama 
        cls() # bersihkan layar setelah keluar dari menu utama

    elif pilihan == "0":
        print("Terima kasih sudah menggunakan sistem.")
        break # keluar dari loop (program selesai)

    else:
        print("Menu tidak valid.")