from structures.circular_linked_list import CircularLinkedList

class Rekomendasi_Sistem:
    def __init__(self, sistem):
        self.sistem = sistem
        self.rekomendasi = CircularLinkedList()
        self.load_rekomendasi()

    def load_rekomendasi(self):
        user = self.sistem.user_login
        if not user:
            return

        genre_favorit = user.minat_genre.lower()
        genre_terkait = [g.lower() for g in self.sistem.genre_graph.get_relasi(genre_favorit)]

        for konser in self.sistem.konser_list:
            genre_konser = konser["genre"].lower()
            if (genre_konser == genre_favorit or genre_konser in genre_terkait):
                self.rekomendasi.append(f"{konser['artis']} - {konser['genre']}")

    def tampilkan_rekomendasi(self):
        rekomendasi = self.rekomendasi.next_promo()
        if rekomendasi:
            print(f"REKOMENDASI: {rekomendasi}")
        else:
            print("Belum ada rekomendasi konser.")