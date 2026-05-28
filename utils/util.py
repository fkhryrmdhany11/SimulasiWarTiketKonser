# fungsi-sungsi pembantu (yang dipakai untuk mencetak header, 
# garis pembatas, dan membersihkan layar terminal)

import os

def print_header(title):
    print("=" * 60)
    print(title.center(60)) # .center(60) -> teks diletakkan di tengah dari 60 karakter
    print("=" * 60)

def pembatas():
    print("=" * 60)

def cls(): 
    """
    membersihkan layar terminal
    """
    os.system("cls")

def verif(): 
    """
    - Menunggu user menekan enter sebelum melanjutkan, lalu membersihkan layar
    - Dipakai setelah menampilkan hasil agar user sempat membaca sebelum layar bersih
    """
    input("\nTekan Enter untuk lanjut...")
    cls()

def print_section(title):
    panjang = 60
    garis = (panjang - len(title) - 2) // 2
    print(f"\n{'-' * garis} {title} {'-' * garis}\n")