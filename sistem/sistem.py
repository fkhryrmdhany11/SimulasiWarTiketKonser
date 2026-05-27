import json
from utils.util import print_header, cls
from models.user import User
from models.graph import GenreGraph
from utils.path import USERS_FILE, KONSER_FILE

# =========================
# SISTEM WAR TIKET
# =========================

class SistemWarTiket:
    def __init__(self):
        self.users = {}
        self.user_login = None
        self.konser_list = []
        self.booked_seats = set()
        self.genre_graph = GenreGraph()
        self.genre_graph.load_graph()
        self.load_data()
        self.load_konser()

    def generate_seat(self, vip_jumlah, reg_jumlah, harga_vip, harga_reg):
        seats = {}
        # VIP
        for i in range(1, vip_jumlah + 1):
            kode = f"VIP{i}"
            seats[kode] = {"kategori": "VIP",
                           "harga": harga_vip,
                           "booked": False,
                           "username": None}
        # REGULER
        for i in range(1, reg_jumlah + 1):
            kode = f"REG{i}"
            seats[kode] = {"kategori": "REGULER",
                           "harga": harga_reg,
                           "booked": False,
                           "username": None}
        return seats
    
    # =========================
    # REGISTER
    # =========================

    def register(self):
        cls()
        print_header("REGISTER")

        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in self.users:
            print("User sudah ada")
            return None

        user = User(username, password)
        self.users[username] = user
        self.user_login = user
        self.save_data()
        print("Register berhasil")
        return user

    # =========================
    # LOGIN
    # =========================

    def login(self):
        cls()
        print_header("LOGIN")

        username = input("Username: ")
        password = input("Password: ")

        user = self.users.get(username)

        if user and user.password == password:
            self.user_login = user
            print(f"Selamat datang {username}")
            return True
        else:
            print("Login gagal")
            return False

    # =========================
    # SAVE DATA
    # =========================

    def save_data(self):
        data = {}
        for username, user in self.users.items():
            history_list = []
            current = user.history.head

            while current:
                history_list.append(current.data)
                current = current.next

            data[username] = {"password": user.password,
                              "minat_genre": user.minat_genre,
                              "history": history_list}

        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # =========================
    # LOAD DATA
    # =========================

    def load_data(self):
        try:
            with open(USERS_FILE, "r") as file:
                data = json.load(file)

                for username, info in data.items():
                    user = User(username, info["password"])
                    user.minat_genre = info.get("minat_genre", "")
                    for transaksi in info.get("history", []):
                        user.history.append(transaksi)
                    self.users[username] = user

        except FileNotFoundError:
            pass
    
    def load_konser(self):
        with open(KONSER_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.konser_list = []

        for konser in data:
            if "seats" not in konser:
                konser["seats"] = self.generate_seat(konser["vip_seat"], 
                                                     konser["reg_seat"], 
                                                     konser["harga_vip"], 
                                                     konser["harga_reg"])
            self.konser_list.append(konser)
    
    # =========================
    # SAVE KONSER
    # =========================
    def save_konser(self):
        with open(KONSER_FILE, "w", encoding="utf-8") as file:
            json.dump(self.konser_list,file, indent=4, ensure_ascii=False)