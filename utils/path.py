# file ini mendefinisikan lokasi file-file data (json)

import os

# os.path.dirname(__file__) -> ambil folder tempat file path.py berada(di folder utils)
# os.path.dirname(...) lagi -> naik satu level ke folder root proyek
BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

# lokasi file data user
USERS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.json"
)

# lokasi file data konser
KONSER_FILE = os.path.join(
    BASE_DIR,
    "data",
    "konser.json"
)

# lokasi file relasi antar genre (sistem rekomendasi berbasis graph)
GRAPH_FILE = os.path.join(
    BASE_DIR,
    "data",
    "relasi_genre.json"
)