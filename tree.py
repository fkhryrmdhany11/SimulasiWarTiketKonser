import json
from sort import sort_artis
import util as ut

# =========================
# NODE GENRE
# =========================

class GenreNode:
    def __init__(self, genre):
        self.genre = genre
        self.konser_list = []
        self.left = None
        self.right = None

# =========================
# TREE GENRE
# =========================

class GenreTree:
    def __init__(self):
        self.root = None

    # =========================
    # INSERT GENRE
    # =========================

    def insert_genre(self, root, genre, konser):

        # Jika node kosong
        if root is None:
            node = GenreNode(genre)
            node.konser_list.append(konser)
            return node

        # Jika genre sama
        if genre == root.genre:
            root.konser_list.append(konser)

        # Jika genre lebih kecil
        elif genre < root.genre:
            root.left = self.insert_genre(
                root.left,
                genre,
                konser
            )

        # Jika genre lebih besar
        else:
            root.right = self.insert_genre(
                root.right,
                genre,
                konser
            )

        return root

    # =========================
    # TAMBAH KONSER
    # =========================

    def tambah_konser(self, konser):

        # Pastikan key genre ada
        if "genre" not in konser:
            return

        genre = konser["genre"]

        self.root = self.insert_genre(
            self.root,
            genre,
            konser
        )

    # =========================
    # TAMPILKAN TREE
    # =========================

    def tampilkan(self, root):

        if root is not None:

            # Traversal kiri
            self.tampilkan(root.left)

            ut.print_header(f"{root.genre.upper()}")

            # Urutkan artis berdasarkan abjad
            artis_sorted = sort_artis(root.konser_list)

            for konser in artis_sorted:

                print(f"Artis          : {konser['artis']}")
                print(f"Tanggal        : {konser['tanggal']}")
                print(f"Tempat         : {konser['tempat']}")
                print(f"Harga Tiket    : Rp{konser['harga']}")
                print(f"Seat Tersedia  : {konser['seat_tersedia']}\n")
                # print("-" * 60)

            # Traversal kanan
            self.tampilkan(root.right)


# =========================
# LOAD JSON
# =========================

def load_konser(filename="konser.json"):

    with open(filename, "r", encoding="utf-8") as file:
        data_konser = json.load(file)

    pohon_genre = GenreTree()

    for konser in data_konser:
        pohon_genre.tambah_konser(konser)

    return pohon_genre