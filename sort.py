def sort_artis(data):

    if len(data) <= 1:
        return data

    tengah = len(data) // 2

    kiri = sort_artis(data[:tengah])
    kanan = sort_artis(data[tengah:])

    return merge_artis(kiri, kanan)


def merge_artis(kiri, kanan):

    hasil = []

    i = 0
    j = 0

    while i < len(kiri) and j < len(kanan):

        artis_kiri = kiri[i]["artis"].lower()
        artis_kanan = kanan[j]["artis"].lower()

        if artis_kiri < artis_kanan:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1

    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1

    return hasil