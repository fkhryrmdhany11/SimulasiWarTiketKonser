from utils.util import print_header, cls
from utils.path import KONSER_FILE
from models.tree import load_konser
from utils.search import LinearSearch
import json

with open(KONSER_FILE, "r") as file:
    data_konser = json.load(file)

# Lihat konser
def tampilkan_konser():
    cls()
    pohon_genre = load_konser()
    pohon_genre.tampilkan(pohon_genre.root)

#Mencari konser
def cari_konser(): #Searching menggunakan linear search karena data yang digunakan adalah dict
    LinearSearch()