# implementasi algoritma merge sort untuk mengurutkan 
# daftar konser berdasarkan nama artis (A-Z)

def sort_artis(data):
    """
    - Mengurutkan list konser berdasarkan nama artis menggunakan merge sort secara rekursif
    - parameter data: list of dict (setiap dict adalah data satu konser)
    """

    if len(data) <= 1: # base case
        return data

    # cari titik tengah untuk membagi ist menjadi dua
    tengah = len(data) // 2

    # (rekursi) urutkan bagian kiri dan kanan secara terpisah
    kiri = sort_artis(data[:tengah])
    kanan = sort_artis(data[tengah:])

    # gabungkan dua bagian yang sudah terurut
    return merge_artis(kiri, kanan)


def merge_artis(kiri, kanan):
    """
    menggabungkan dua list yang usdah terurut menjadi satu
    """

    hasil = [] # list hasil penggabungan

    i = 0 # index pointer untuk list kiri
    j = 0 # index pointer untuk list kanan

    # selama kedua list masih ada isinya, bandingkan elemen terdepan
    while i < len(kiri) and j < len(kanan):
        # ambil nama artis dari masing-masing list
        artis_kiri = kiri[i]["artis"].lower()
        artis_kanan = kanan[j]["artis"].lower()

        if artis_kiri < artis_kanan:
            # jika artis kiri lebih awal di alfabet, maka maasukkan ke hasil
            hasil.append(kiri[i])
            i += 1
        else:
            # jika artis kanan lebih awal di alfabet, maka masukkan ke hasil
            hasil.append(kanan[j])
            j += 1

    # tambahkan sisa elemen dari list kiri (jika masih ada)
    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1
    # tambahkan sisa elemen dari list kanan (jika masih ada)
    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1

    # kembalikan hasil yang sudah digabung dan terurut
    return hasil
