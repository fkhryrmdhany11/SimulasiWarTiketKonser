import util as ut
import json
from tree import load_konser

def menu_daftar_konser():
    ut.cls()
    while True:
        ut.print_header("DAFTAR KONSER")
        print("1. Rekomendasi Konser")
        print("2. Searching Konser")
        print("3. Tampilkan Konser")
        print("0. Keluar")
        ut.pembatas()

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            pass

        elif pilihan == "2":
            cari_konser()
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

        elif pilihan == "3":
            tampilkan_konser()
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

        elif pilihan == "0":
            break

        else:
            print("Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            ut.cls()

with open("konser.json", "r") as file:
    data_konser = json.load(file)


# Lihat konser
def tampilkan_konser():
    ut.cls()
    pohon_genre = load_konser()
    pohon_genre.tampilkan(pohon_genre.root)

#Mencari konser
def cari_konser(): #Searching menggunakan linear search karena data yang digunakan adalah dict
    ut.cls()
    ut.print_header("PENCARIAN")
    keyword = str(input("Masukkan keyword: "))
    ditemukan = False
    area_pencarian = ["artis", "genre", "tempat"]
    print()
    ut.print_header("HASIL PENCARIAN")

    for konser in data_konser:
        for value in area_pencarian:
            if keyword.lower() in str(konser[value]).lower():

                ditemukan = True
                
                print(f"\nNama Artis     : {konser['artis']}")
                print(f"Tanggal        : {konser['tanggal']}")
                print(f"Genre          : {konser['genre']}")
                print(f"Harga Tiket    : Rp {konser['harga']}")
                print(f"Tempat         : {konser['tempat']}")
                print(f"Seat Tersedia  : {konser['seat_tersedia']}")
                break

    if not ditemukan:
        print("Konser tidak ditemukan!")