import json
from utils.util import print_header, cls
from models.user import User
from utils.path import USERS_FILE, KONSER_FILE

# =========================
# SISTEM WAR TIKET
# =========================

class SistemWarTiket:
    def __init__(self):
        self.users = {}
        self.user_login = None
        self.konser_list = []
        self.load_konser()

    def generate_seat(self,
                    vip_jumlah,
                    reg_jumlah,
                    harga_vip,
                    harga_reg):

        seats = {}

        # VIP
        for i in range(1, vip_jumlah + 1):

            kode = f"VIP{i}"

            seats[kode] = {
                "kategori": "VIP",
                "harga": harga_vip,
                "booked": False,
                "username": None
            }

        # REGULER
        for i in range(1, reg_jumlah + 1):

            kode = f"REG{i}"

            seats[kode] = {
                "kategori": "REGULER",
                "harga": harga_reg,
                "booked": False,
                "username": None
            }

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
            return

        self.users[username] = User(username, password)

        self.save_data()

        print("Register berhasil")

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
            data[username] = {
                "password": user.password
            }

        with open(USERS_FILE, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # =========================
    # LOAD DATA
    # =========================

    def load_data(self):
        try:
            with open(USERS_FILE, "r") as file:
                data = json.load(file)

                for username, info in data.items():
                    self.users[username] = User(username, info["password"])

        except FileNotFoundError:
            pass
    
    def load_konser(self):

        with open(KONSER_FILE, "r") as file:

            data = json.load(file)

        for konser in data:

            konser["seats"] = self.generate_seat(
                konser["vip_seat"],
                konser["reg_seat"],
                konser["harga_vip"],
                konser["harga_reg"]
            )

            self.konser_list.append(konser)