import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

USERS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.json"
)

KONSER_FILE = os.path.join(
    BASE_DIR,
    "data",
    "konser.json"
)

GRAPH_FILE = os.path.join(
    BASE_DIR,
    "data",
    "relasi_genre.json"
)