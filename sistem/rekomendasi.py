# Sistem Rekomendasi Konser
# dipakai untuk memberikan rekomendasi konser berdasarkan genre favorit user

from structures.circular_linked_list import CircularLinkedList

class Rekomendasi_Sistem:
    def __init__(self, sistem):
        self.sistem = sistem # refrensi ke sistem utama
        self.rekomendasi = CircularLinkedList() # list circular berisi konser rekomendasi
        self.load_rekomendasi() # isi list saat objek dibuat

    def load_rekomendasi(self):
        """
        Mengisi CircularLinkedList dengan konser-konser yang
        relevan berdasarkan genre favorit user

        Konser dianggap relevan jika:
        - Genre-nya sama persis dengan genre favorit user, atau
        - Genre-nya berelasi dengan genre favorit (dari Graf)
        """
        user = self.sistem.user_login
        if not user: # jika tidak ada user yang login, maka tidak ada rekomendasi
            return

        genre_favorit = user.minat_genre.lower()

        # ambil genre-genre yang berkaitan dari graph, ubah ke lowercase
        genre_terkait = [g.lower() for g in self.sistem.genre_graph.get_relasi(genre_favorit)]

        # cek setiap konser, masukkan ke rekomendasi jika genrenya cocok
        for konser in self.sistem.konser_list:
            genre_konser = konser["genre"].lower()
            if (genre_konser == genre_favorit or genre_konser in genre_terkait):
                self.rekomendasi.append(f"{konser['artis']} - {konser['genre']}")

    def tampilkan_rekomendasi(self):
        """
        - Menampilkan satu rekomendasi konser (berputar setiap kali dipanggil)
        - Jika tidak ada rekomendasi, tampilkan pesan default
        """
        rekomendasi = self.rekomendasi.next_promo()
        if rekomendasi:
            print(f"REKOMENDASI: {rekomendasi}")
        else:
            print("Belum ada rekomendasi konser.")