# =========================================
# BAGIAN A — FUNGSI DAN LOGIKA PROGRAM
# =========================================

def generate_angka(seed):
    """Menghasilkan angka target berdasarkan seed tanpa random."""
    angka = (seed * 7 + 3) % 10 + 1
    return angka


def cek_tebakan(tebakan, target):
    """Mengecek hasil tebakan terhadap target."""
    if tebakan == target:
        return "Benar"
    elif tebakan < target:
        return "Terlalu kecil"
    else:
        return "Terlalu besar"


def main_game(nama, seed):
    """Menjalankan permainan tebak angka dan mengembalikan skor."""
    target = generate_angka(seed)
    skor = 0

    for i in range(1, 4):  # 3 percobaan
        tebakan = int(input(f"Percobaan ke-{i}, masukkan tebakan (1-10): "))
        hasil = cek_tebakan(tebakan, target)
        print(hasil)

        if hasil == "Benar":
            if i == 1:
                skor = 100
            elif i == 2:
                skor = 70
            else:
                skor = 50
            break
    else:
        print(f"Gagal! Angka yang benar adalah {target}")
        skor = 0

    return {
        "nama": nama,
        "skor": skor
    }


def simpan_riwayat(riwayat, hasil):
    """Menyimpan hasil permainan ke dalam list riwayat."""
    riwayat.append(hasil)
    return riwayat


# =========================================
# BAGIAN B — MATRIX 2D
# =========================================

def buat_matrix(riwayat):
    """Mengubah riwayat menjadi matrix 2D."""
    if len(riwayat) == 0:
        return []

    matrix = [["Nama", "Skor"]]

    for data in riwayat:
        matrix.append([data["nama"], data["skor"]])

    return matrix


def tampilkan_tabel(matrix):
    """Menampilkan matrix dalam bentuk tabel."""
    if len(matrix) == 0:
        print("Data kosong")
        return

    for baris in matrix:
        for kolom in baris:
            print(f"{kolom:<10}", end=" ")
        print()


# =========================================
# BAGIAN C — SELECTION SORT
# =========================================

def urutkan_leaderboard(data):
    """Mengurutkan data berdasarkan skor secara descending (selection sort)."""
    hasil = data.copy()  # salinan agar tidak mengubah data asli
    n = len(hasil)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if hasil[j]["skor"] > hasil[max_idx]["skor"]:
                max_idx = j

        # Tukar posisi
        hasil[i], hasil[max_idx] = hasil[max_idx], hasil[i]

    return hasil


def tampilkan_leaderboard(data):
    """Menampilkan leaderboard dengan peringkat."""
    if len(data) == 0:
        print("Belum ada data")
        return

    print("\n=== LEADERBOARD ===")
    for i in range(len(data)):
        print(f"{i+1}. {data[i]['nama']} - {data[i]['skor']}")


# =========================================
# PROGRAM UTAMA
# =========================================

def main():
    """Program utama untuk menjalankan seluruh sistem."""
    riwayat = []
    seed = 1

    while True:
        print("\n=== MENU ===")
        print("1. Main Game")
        print("2. Lihat Riwayat")
        print("3. Lihat Leaderboard")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            hasil = main_game(nama, seed)
            riwayat = simpan_riwayat(riwayat, hasil)
            seed += 1

        elif pilihan == "2":
            matrix = buat_matrix(riwayat)
            tampilkan_tabel(matrix)

        elif pilihan == "3":
            data_urut = urutkan_leaderboard(riwayat)
            tampilkan_leaderboard(data_urut)

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


# Menjalankan program
main()