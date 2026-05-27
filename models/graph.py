import json
from utils.path import GRAPH_FILE


class GenreGraph:

    def __init__(self):
        self.graph = {}
        # otomatis load graph saat object dibuat
        self.load_graph()

    # load graph dari json
    def load_graph(self):
        try:
            with open(GRAPH_FILE, "r", encoding="utf-8") as file:
                self.graph = json.load(file)

        except FileNotFoundError:
            print("File relasi_genre.json tidak ditemukan.")
            self.graph = {}

        except json.JSONDecodeError:
            print("Format JSON relasi genre salah.")
            self.graph = {}

    # tambah relasi
    def tambah_relasi(self, genre1, genre2):
        genre1 = genre1.upper()
        genre2 = genre2.upper()

        if genre1 not in self.graph:
            self.graph[genre1] = []

        if genre2 not in self.graph[genre1]:
            self.graph[genre1].append(genre2)

    # ambil relasi
    def get_relasi(self, genre):
        genre = genre.upper()
        return self.graph.get(genre, [])