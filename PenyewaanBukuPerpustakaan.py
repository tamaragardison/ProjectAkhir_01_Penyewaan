user_data = {}  

def login(user_data):
    print("\n=== Login ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username in user_data and user_data[username] == password:
        print("Login berhasil!", username)
        return True
    print("Username atau password salah")
    return False

def register(user_data):
    print("\n=== Registrasi Pengguna Baru ===")
    while True:
        username = input("Masukkan Username baru: ")
        password = input("Masukkan Password baru: ")

        if not username or not password:
            print("Tolong masukkan username atau password")
            continue

        if username in user_data:
            print("Username sudah digunakan")
        else:
            user_data[username] = password
            print("Registrasi berhasil!")
            return
        
def menu():
    print("\n=== Menu Peminjaman Buku ===")
    print("1. Tambah Peminjaman Buku")
    print("2. Lihat Peminjaman Buku")
    print("3. Hapus Peminjaman Buku")
    print("4. Update Peminjaman Buku")
    print("5. Cari peminjaman Buku")
    print("6. Cetak Data Buku")
    print("7. Logout")

def cari_peminjaman(peminjaman_list):
    print("\n=== Cari Data Peminjaman ===")
    print("1. Cari berdasarkan ID Peminjaman")
    print("2. Cari berdasarkan Nama Peminjam")
    print("3. Cari berdasarkan Judul Buku")
    pilihan = input("Pilih metode pencarian (1-3): ")

    if pilihan == "1":
        id_peminjaman = int(input("Masukkan ID Peminjaman: "))
        hasil = [peminjaman for peminjaman in peminjaman_list if peminjaman["ID peminjaman"] == id_peminjaman]
    elif pilihan == "2":
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        hasil = [peminjaman for peminjaman in peminjaman_list if peminjaman["Nama peminjam"] == nama_peminjam]
    elif pilihan == "3":
        judul_buku = input("Masukkan Judul Buku: ")
        hasil = [peminjaman for peminjaman in peminjaman_list if peminjaman["Judul buku"] == judul_buku]
    else:
        print("Pilihan tidak valid")
        return

    if hasil:
        print("\n=== Hasil Pencarian ===")
        for peminjaman in hasil:  
            print(f"ID Peminjaman    : {peminjaman['ID peminjaman']}")
            print(f"Nama Peminjam    : {peminjaman['Nama peminjam']}")
            print(f"Judul Buku       : {peminjaman['Judul buku']}")
            print(f"Nomor Buku       : {peminjaman['Nomor buku']}")
            print(f"Tanggal Peminjaman: {peminjaman['Tanggal peminjaman']}\n")
    else:
        print("Data tidak ditemukan")

def tambah_peminjaman(peminjaman_list):
    print("\n=== Tambah Peminjaman Buku ===")
    digunakan_id = {peminjaman["ID peminjaman"] for peminjaman in peminjaman_list}  # Himpunan untuk menyimpan ID yang sudah ada

    while True:
        while True:
            id_peminjaman = int(input("Masukkan ID Peminjaman: "))
            if id_peminjaman:
                if id_peminjaman in digunakan_id:
                    print("ID Peminjaman sudah digunakan, masukkan ID lain")
                else:
                    digunakan_id.add(id_peminjaman)  
                    break
            else:
                print("ID Peminjaman tidak boleh kosong")

        while True:
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            if nama_peminjam:
                break
            print("Nama Peminjam tidak boleh kosong")

        while True:
            judul_buku = input("Masukkan Judul Buku: ")
            if judul_buku:
                break
            print("Judul Buku tidak boleh kosong")

        while True:
            no_buku = int(input("Masukkan Nomor Buku: "))
            if no_buku:
                break
            print("Nomor Buku tidak boleh kosong")

        while True:
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
            if tanggal_peminjaman:
                break
            print("Tanggal Peminjaman tidak boleh kosong")

        peminjaman = {
            "ID peminjaman": id_peminjaman,
            "Nama peminjam": nama_peminjam,
            "Judul buku": judul_buku,
            "Nomor buku": no_buku,
            "Tanggal peminjaman": tanggal_peminjaman,
        }
        peminjaman_list.append(peminjaman)
        print("Data peminjaman berhasil ditambahkan")

        tambah_lagi = input("Apakah Anda ingin menambah data peminjaman lagi? (ya/tidak): ")
        if tambah_lagi.lower() != 'ya':
            break


def hapus_peminjaman(peminjaman_list):
    print("\n=== Hapus Peminjaman Buku ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for peminjaman in peminjaman_list:
        if peminjaman["ID peminjaman"] == id_peminjaman:  
            peminjaman_list.remove(peminjaman)
            print("Data peminjaman berhasil dihapus")
            return
    print("Data peminjaman tidak ditemukan")

def update_peminjaman(peminjaman_list):
    print("\n=== Update Peminjaman Buku ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin di-update: ")
    for peminjaman in peminjaman_list:
        if peminjaman["ID peminjaman"] == id_peminjaman: 
            print("\nData lama:")
            print(f"ID Peminjaman    : {peminjaman['ID peminjaman']}")
            print(f"Nama Peminjam    : {peminjaman['Nama peminjam']}")
            print(f"Judul Buku       : {peminjaman['Judul buku']}")
            print(f"Nomor Buku       : {peminjaman['Nomor buku']}")
            print(f"Tanggal Peminjaman: {peminjaman['Tanggal peminjaman']}")

            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            no_buku = input("Masukkan Nomor Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (DD-MM-YYYY): ")

            if nama_peminjam:
                peminjaman["Nama peminjam"] = nama_peminjam
            if judul_buku:
                peminjaman["Judul buku"] = judul_buku
            if no_buku:
                peminjaman["Nomor buku"] = no_buku
            if tanggal_peminjaman:
                peminjaman["Tanggal peminjaman"] = tanggal_peminjaman

            print("\nData peminjaman berhasil di-update.")
            return

    print("Data peminjaman dengan ID tersebut tidak ditemukan")

def cetak(peminjaman_list):
    print("\n=== Cetak Data Peminjaman ===")

    if not peminjaman_list:
        print("Belum ada data peminjaman.")
        return

    for peminjaman in peminjaman_list:
        print(f"ID Peminjaman    : {peminjaman['ID peminjaman']}")
        print(f"Nama Peminjam    : {peminjaman['Nama peminjam']}")
        print(f"Judul Buku       : {peminjaman['Judul buku']}")
        print(f"Nomor Buku       : {peminjaman['Nomor buku']}")
        print(f"Tanggal Peminjaman: {peminjaman['Tanggal peminjaman']}")

        lama_peminjaman = int(input(f"Masukkan lama peminjaman (hari) untuk ID {peminjaman['ID peminjaman']}: "))

        if lama_peminjaman > 7:
            keterlambatan = lama_peminjaman - 7
            denda_total = keterlambatan * 2000
        print(f"Denda Keterlambatan: Rp {denda_total}\n")

def main():
    peminjaman_list = []

    while True:
        print("\n=== Sistem Peminjaman Buku ===")
        print("1. Login")
        print("2. Registrasi Pengguna Baru")
        print("3. Keluar")
        pilihan = input("Silahkan Pilih Menu (1-3): ")

        if pilihan == "1":
            if login(user_data):
                print("Login berhasil!")
                while True:
                    menu()
                    pilihan_menu = input("Silahkan Pilih Menu (1-7): ")

                    if pilihan_menu == "1":
                        tambah_peminjaman(peminjaman_list)
                    elif pilihan_menu == "2":
                        print("\n=== Data Peminjaman Buku ===")
                        if peminjaman_list:
                            for peminjaman in peminjaman_list:
                                print(f"ID Peminjaman   : {peminjaman['ID peminjaman']}")
                                print(f"Nama Peminjam   : {peminjaman['Nama peminjam']}")
                                print(f"Buku yang Dipinjam: {peminjaman['Judul buku']}")
                                print(f"Nomor Buku      : {peminjaman['Nomor buku']}")
                                print(f"Tanggal Peminjaman: {peminjaman['Tanggal peminjaman']}\n")
                        else:
                            print("Belum ada data peminjaman")
                    elif pilihan_menu == "3":
                        hapus_peminjaman(peminjaman_list)
                    elif pilihan_menu == "4":
                        update_peminjaman(peminjaman_list)
                    elif pilihan_menu == "5":
                       cari_peminjaman(peminjaman_list)
                    elif pilihan_menu == "6":
                        cetak(peminjaman_list)
                    elif pilihan_menu == "7":
                        print ("Anda telah logout")
                        break
            else:
                print("Login gagal")
        elif pilihan == "2":
            register(user_data)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem peminjaman buku!")
            break
        else:
            print("Pilihan tidak valid")

main()