# --- BAGIAN A: FUNGSI DAN LOGIKA PROGRAM ---

def hitung_skor(benar, salah):
    """Menghitung total skor berdasarkan jumlah jawaban benar dan salah."""
    # Logika kondisional untuk menghitung poin 
    poin = (benar * 10) - (salah * 5)
    
    # Memastikan skor tidak negatif
    if poin < 0:
        return 0
    return poin

def mainkan_game(nama_pemain):
    """Menjalankan logika permainan untuk satu pemain dan mengembalikan data dalam list."""
    print(f"\n--- Halo {nama_pemain}, selamat bermain! ---")
    
    # Input dari pengguna dalam loop [cite: 4, 14]
    jawaban_benar = int(input("Masukkan jumlah jawaban benar: "))
    jawaban_salah = int(input("Masukkan jumlah jawaban salah: "))
    
    # Memanggil fungsi lain di dalam fungsi 
    total_skor = hitung_skor(jawaban_benar, jawaban_salah)
    
    # Mengembalikan hasil berupa list 
    return [nama_pemain, total_skor]

# --- BAGIAN B: STRUKTUR DATA LIST DAN MATRIX 2D ---

def tampilkan_leaderboard(data_skor):
    """Menampilkan data list 2D dalam format tabel yang rapi."""
    # Menangani kondisi list kosong 
    if not data_skor:
        print("\n[Peringatan] Belum ada data pemain!")
        return

    print("\n" + "="*25)
    print(f"{'Rank':<5} {'Nama':<12} {'Skor':<5}")
    print("-" * 25)
    
    # Melakukan iterasi pada matrix 2D 
    peringkat = 1
    for baris in data_skor:
        nama = baris[0] # Mengakses elemen index 0 
        skor = baris[1] # Mengakses elemen index 1 
        print(f"{peringkat:<5} {nama:<12} {skor:<5}")
        peringkat += 1
    print("="*25)

# --- BAGIAN C: ALGORITMA PENGURUTAN MANUAL ---

def urutkan_skor_descending(data_asli):
    """Mengurutkan data menggunakan Selection Sort tanpa mengubah data asli."""
    # Membuat salinan data agar data asli tidak berubah (In-place vs Copy) 
    data_copy = []
    for item in data_asli:
        data_copy.append(item[:]) # Salinan mendalam (deep copy) sederhana

    n = len(data_copy)
    
    # Implementasi Selection Sort manual 
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            # Membandingkan nilai skor (index 1) untuk pengurutan terbesar ke terkecil
            if data_copy[j][1] > data_copy[max_idx][1]:
                max_idx = j
        
        # Tukar posisi (swap) secara manual 
        data_copy[i], data_copy[max_idx] = data_copy[max_idx], data_copy[i]
        
    return data_copy

# --- PROGRAM UTAMA: ALUR DAN INTEGRASI ---

def main():
    """Mengatur alur utama program dari input hingga leaderboard."""
    database_pemain = [] # Matrix 2D untuk menyimpan [nama, skor] [cite: 6]
    
    # Perulangan while untuk memproses input berulang [cite: 14]
    while True:
        nama = input("\nMasukkan nama pemain (atau ketik 'selesai' untuk keluar): ")
        if nama.lower() == 'selesai':
            break
        
        # Integrasi fungsi permainan [cite: 14, 15]
        hasil_pemain = mainkan_game(nama)
        database_pemain.append(hasil_pemain)
    
    # Menampilkan hasil akhir [cite: 12, 14]
    if database_pemain:
        print("\nMemproses Leaderboard...")
        leaderboard_terurut = urutkan_skor_descending(database_pemain)
        tampilkan_leaderboard(leaderboard_terurut)
    else:
        tampilkan_leaderboard([])

# Menjalankan program utama
if __name__ == "__main__":
    main()