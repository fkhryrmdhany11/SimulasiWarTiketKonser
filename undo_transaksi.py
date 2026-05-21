# algo:
# masuk ke method, baca file histori transaksi (nama file smntr: histori.json), cari transaksi terakhir user,
# hapus transaksi terakhir itu, kembalikan seatnya (jd avail lg), simpan ulang json, kurang lebih gitu

import json

class UndoTransaksi:
    
    def batalkan(self, username):
        # baca file histori dulu
        with open("histori.json", "r") as f:
            histori = json.load(f)

        transaksi_terakhir = None

        # cari transaksi terakhir user
        for transaksi in reversed(histori):
            if transaksi['username'] == username:
                transaksi_terakhir = transaksi
                break

        if transaksi_terakhir is None:
            print('Tidak ada transaksi yang dapat dibatalkan')
            return

        # hapus transaksi
        histori.remove(transaksi_terakhir)

        #simpan ulang histori
        with open("history.json", "w") as f:
            json.dump(histori, f, indent = 4)

        # baca data konser
        with open("histori.json", "r") as f:
            data_konser = json.load(f)

        # kembalikan seat
        # simpan ulang data        