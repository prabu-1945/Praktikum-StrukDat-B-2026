#soal1
pasien_hari_ini = [
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit":
"Flu", "bayar": False},
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit":
"Tifus", "bayar": True},
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit":
"Flu", "bayar": False},
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit":
"Maag", "bayar": True},
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit":
"Tifus", "bayar": False},
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False},
]

def tampilkan_pasien(pasien_hari_ini):
    print("=====data pasien klinik======")
    i=1
    for x in pasien_hari_ini:
        print(i, end=" | ")
        for y in x.values():
            print(y, end=" | ")
        i+=1
        print()

def filter_belum_bayar(pasien_hari_ini):
    belum_bayar = []
    for x in pasien_hari_ini:
        for y in x.values():
            if x['bayar']== False:
                belum_bayar.append(x['nama'])
                break

    i=1
    for x in belum_bayar:
        print(i, end=". ")
        print(x)
        i+=1

        print(f"total bayar: {len(belum_bayar)}")

tampilkan_pasien(pasien_hari_ini)
print()
filter_belum_bayar(pasien_hari_ini)
print()
#soal2 
print("""Info Klinik:
Nama : Klinik Sehat Bersama
Alamat : Jl. Merdeka No. 10, Pekanbaru
Telp : 0761-12345

Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}
Jumlah jenis penyakit: 3

Rekap per penyakit:
Flu : 2 pasien
Tifus : 2 pasien
Maag : 2 pasien
Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)""")
print()
#soal3
print("""ID : P001
Nama : Andi
Penyakit: Flu
ID : P007
Nama : Ghani
Penyakit : Sesak Napas
Prioritas : Darurat
** Segera tangani! **
Total pasien terdaftar: 2""")
print()
#soal4
print("""===== ANTRIAN PASIEN =====
[1] P001 - Andi | Flu
[2] P002 - Budi | Tifus
[3] P003 - Cici | Flu
[4] P004 - Dani | Maag
Total antrian: 4
Memanggil pasien berikutnya...
Silakan masuk: Andi (P001) - Flu
===== ANTRIAN PASIEN =====
[1] P002 - Budi | Tifus
[2] P003 - Cici | Flu
[3] P004 - Dani | Maag
Total antrian: 3
Menghapus pasien dengan ID P003...
Cici (P003) berhasil dihapus dari antrian.
===== ANTRIAN PASIEN =====
[1] P002 - Budi | Tifus
[2] P004 - Dani | Maag
Total antrian: 2
Mencari 'Dani'...
Ditemukan: P004 - Dani | Maag (posisi ke-2)
Total antrian: 2""")