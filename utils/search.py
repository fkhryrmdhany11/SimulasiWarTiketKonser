# implementasi linear search untuk pencarian konser

from utils.util import print_header, cls
from utils.path import KONSER_FILE
import json

# load data konser dari file json saat modul ini pertama kali diimpor
with open(KONSER_FILE, "r") as file:
    data_konser = json.load(file)

def LinearSearch():
    """
    - Mencari konser berdasarkan keyword yang dimasukkan user
    - Keyword dicocokkan ke tiga field (artis, genre, dan tempat)
    """
    cls()
    print_header("PENCARIAN")
    keyword = str(input("Masukkan keyword: "))
    ditemukan = False

    # field-field yang akan dicari (nama kolom dalam dict konser)
    area_pencarian = ["artis", "genre", "tempat"]
    print()
    print_header("HASIL PENCARIAN")

    for konser in data_konser: # iterasi setiap konser 
        for value in area_pencarian: # cek apakah keyword ada di salah satu field pencarian
            if keyword.lower() in str(konser[value]).lower():

                ditemukan = True
                # tampilkan detail konser yang cocok
                print(f"Artis          : {konser['artis']}")
                print(f"Tanggal        : {konser['tanggal']}")
                print(f"Tempat         : {konser['tempat']}")
                print(f"Harga Tiket    : Rp{konser['harga_reg']:,} - " f"Rp{konser['harga_vip']:,}")
                print(f"VIP Seat       : {konser['vip_seat']}")
                print(f"Regular Seat   : {konser['reg_seat']}\n")
                break 
                # agar konser yang sama tidak ditampilkan dua kali jika keyword cocok lebih dr satu field

    if not ditemukan:
        print("Konser tidak ditemukan!")