import json
import util as ut
import menu as main

# =========================
# CLASS USER
# =========================

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# =========================
# SISTEM WAR TIKET
# =========================

class SistemWarTiket:
    def __init__(self):
        self.users = {}
        self.user_login = None
        self.load_data()

    # =========================
    # REGISTER
    # =========================

    def register(self):
        ut.cls()
        ut.print_header("REGISTER")

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
        ut.cls()
        ut.print_header("LOGIN")

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

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # =========================
    # LOAD DATA
    # =========================

    def load_data(self):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)

                for username, info in data.items():
                    self.users[username] = User(username, info["password"])

        except FileNotFoundError:
            pass

    def run_app(self):
        ut.cls()
        while True:
            ut.print_header("SISTEM WAR TIKET KONSER")
            print("1. Masuk")
            print("0. Keluar")
            ut.pembatas()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                verif = main.menu_awal(self)
                print(verif)
                print(self.user_login)
                if verif and self.user_login:
                    main.menu_utama(self)
            elif pilihan == "0":
                print("Terima kasih sudah menggunakan sistem.")
                break
            else:
                print("Menu tidak valid.")