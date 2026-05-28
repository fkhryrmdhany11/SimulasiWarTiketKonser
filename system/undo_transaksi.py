# implementasi fitur undo untuk membatalkan transaksi terakhir menggunakan stack

import json

class UndoTransaksi:
    
    def batalkan(self, username):
        # baca file histori dulu
        with open("user.json", "r") as f:
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
        with open("user.json", "w") as f:
            json.dump(histori, f, indent = 4)

        # baca data konser
        with open("user.json", "r") as f:
            data_konser = json.load(f)

        # kembalikan seat
        for konser in data_konser:
            if konser['nama'] == transaksi_terakhir['konser']:
                konser['seat_tersedia'].append(transaksi_terakhir['seat'])
                break
       
        # simpan ulang data
        with open('konser.json', 'w') as f:
            json.dump(data_konser, f, indent=4)               

        
        print("\n=== TRANSAKSI BERHASIL DIBATALKAN ===")
        print(f"Konser : {transaksi_terakhir['konser']}")
        print(f"Seat   : {transaksi_terakhir['seat']}")
        print(f"Harga  : Rp {transaksi_terakhir['harga']}")