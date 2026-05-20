import json

with open("konser.json", "r") as file:
    data_konser = json.load(file)


# Lihat konser
def lihat_konser():

    print("\n===== DAFTAR KONSER =====")

    for i, konser in enumerate(data_konser, start=1):

        print(f"\nKonser {i}")
        print(f"Nama Artis     : {konser['artis']}")
        print(f"Tanggal        : {konser['tanggal']}")
        print(f"Genre          : {konser['genre']}")
        print(f"Harga Tiket    : Rp{konser['harga']}")
        print(f"Tempat         : {konser['tempat']}")
        print(f"Seat Tersedia  : {konser['seat_tersedia']}")

#Mencari konser
def cari_konser(keyword):

    ditemukan = False

    print("\n===== HASIL PENCARIAN =====")

    for konser in data_konser:

        if (keyword.lower() in konser['artis'].lower() or
            keyword.lower() in konser['genre'].lower()):

            ditemukan = True

            print(f"\nNama Artis     : {konser['artis']}")
            print(f"Tanggal        : {konser['tanggal']}")
            print(f"Genre          : {konser['genre']}")
            print(f"Harga Tiket    : Rp{konser['harga']}")
            print(f"Tempat         : {konser['tempat']}")
            print(f"Seat Tersedia  : {konser['seat_tersedia']}")

    if not ditemukan:
        print("Konser tidak ditemukan!")


#Sorting berdasarkan abjad
def sorting_abjad():

    hasil_sort = sorted(
        data_konser,
        key=lambda konser: konser['artis']
    )

    print("\n===== DAFTAR KONSER =====")

    for konser in hasil_sort:
        print(konser['artis'])


#Sorting berdasarkan genre
def sorting_genre():

    hasil_sort = sorted(
        data_konser,
        key=lambda konser: konser['genre']
    )

    print("\n===== DAFTAR KONSER =====")

    for konser in hasil_sort:
        print(f"{konser['genre']} - {konser['artis']}")


#Informasi konser
def info_konser(nama_artis):

    ditemukan = False

    for konser in data_konser:

        if nama_artis.lower() == konser['artis'].lower():

            ditemukan = True

            print("\n===== INFORMASI KONSER =====")
            print(f"Nama Artis     : {konser['artis']}")
            print(f"Tanggal        : {konser['tanggal']}")
            print(f"Genre          : {konser['genre']}")
            print(f"Harga Tiket    : Rp{konser['harga']}")
            print(f"Tempat         : {konser['tempat']}")
            print(f"Seat Tersedia  : {konser['seat_tersedia']}")

            print("Daftar Seat    : ", end="")

            for seat in konser['nama_seat']:
                print(seat, end=" ")

            print()

    if not ditemukan:
        print("Konser tidak ditemukan!")