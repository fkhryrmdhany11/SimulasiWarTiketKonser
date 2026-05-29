# daftar_konser.py (menampilkan dan mencari konser)

from utils.util import print_header, cls
from utils.path import KONSER_FILE
from models.tree import load_konser
from utils.search import LinearSearch
import json

# membaca seluruh data konser dari file json
# data ini akan digunakan dalam fitur penampilan dan pencarian konser
with open(KONSER_FILE, "r") as file:
    data_konser = json.load(file)

def tampilkan_konser():
    """
    Menampilkan semua konser yang dikelompokkan berdasarkan genre,
    diurutkan secara alfabetis menggunakan Binary Search Tree
    """
    cls()
    pohon_genre = load_konser() # memuat data konser ke dalam BST
    pohon_genre.tampilkan(pohon_genre.root) # traversal inorder untuk menampilkan data konser (terurut secara alfabetis)

# Mencari konser
def cari_konser(): 
    """
    - Searching menggunakan linear search karena data yang digunakan adalah dict
    - Searching konser berdasarkan keyword yang dicocokkan ke field artis, genre, dan tempat
    """
    LinearSearch()