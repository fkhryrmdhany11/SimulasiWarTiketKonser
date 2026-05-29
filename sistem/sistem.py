import json
from utils.util import print_header, cls
from models.user import User
from models.graph import GenreGraph
from utils.path import USERS_FILE, KONSER_FILE

# =========================
# SISTEM WAR TIKET
# =========================

class SistemWarTiket:
    """
    - Class utama yang menyimpan seluruh state (kondisi) program
    (semua fitur (booking, history, undo, rekomendasi) bergantung
     pada objek sistem ini sebagai sumber data utama)
    - Satu objek sistem dibuat di main.py dan dipakai sepanjang program
    """

    def __init__(self):
        self.users = {} # dict semua user: {username: User}
        self.user_login = None # user yang sedang login (none jika belum login)
        self.konser_list = [] # list semua konser (list of dict)
        self.booked_seats = set() # set kursi yang sudah dibooking
        
        # graph relasi genre untuk sistem rekomendasi
        self.genre_graph = GenreGraph()  
        self.genre_graph.load_graph() # load relasi genre dari json
        
        # load data user dan konser dari file json
        self.load_data() 
        self.load_konser() 

    # ============================================================
    # GENERATE SEAT - Membuat seat untuk satu konser
    # ============================================================

    def generate_seat(self, vip_jumlah, reg_jumlah, harga_vip, harga_reg):
        """
        - Membuat dictionary kursi (seat) untuk satu konser
        - Dipanggil saat konser belum memiliki data kursi
        """
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
    # REGISTER - Mendaftarkan user baru
    # =========================

    def register(self):
        cls()
        print_header("REGISTER")

        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # cek apakah username sudah dipakai
        if username in self.users:
            print("User sudah ada")
            return None

        # buat user baru lalu simpan ke dict users
        user = User(username, password)
        self.users[username] = user
        self.user_login = user # langsung set sebagai user yang login
        self.save_data() # simpan ke file json
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

        # cari user berdasarkan username
        user = self.users.get(username)

        if user and user.password == password: 
            # jika login berhasil, set user sebagai yang sedang login
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

            # telusuri double linked list dari head ke tail
            current = user.history.head
            while current:
                history_list.append(current.data)
                current = current.next

            # simpan semua atribut user ke dict
            data[username] = {"password": user.password,
                              "minat_genre": user.minat_genre,
                              "history": history_list}

        # tulis ke file json dengan format UTF-8
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            # simpan data ke file dengan jarak 4 spasi dan karakter non ASCII apa adanya
    
    # =========================
    # LOAD DATA
    # =========================

    def load_data(self):
        """
        - Membaca data user dari file users.json 
        dan muat ulang ke dalam objek User di memori
        - Jika file belum ada maka diabaikan"""
        try:
            with open(USERS_FILE, "r") as file:
                data = json.load(file)

                for username, info in data.items():
                    # buat ulang objek User
                    user = User(username, info["password"])
                    user.minat_genre = info.get("minat_genre", "")

                    # muat ulang history ke DLL
                    for transaksi in info.get("history", []):
                        user.history.append(transaksi)
                    self.users[username] = user

        except FileNotFoundError: # jika file belum ada, mulai dengan data kosong
            pass
    
    def load_konser(self):
        
        # membaca semua data konser dari file konser.json
        with open(KONSER_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.konser_list = []

        for konser in data:
            # jika konser belum punya seat, buat daftar kursi konser secara otomatis
            # dari jumlah seat dan harga yang sudah ditentukan
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
        """
        - Menyimpan kondisi terbaru semua konser (termasuk status booking kursi)
        ke file konser.json
        - Dipanggil setiap kali ada booking atau undo transaksi
        """
        with open(KONSER_FILE, "w", encoding="utf-8") as file:
            json.dump(self.konser_list,file, indent=4, ensure_ascii=False)