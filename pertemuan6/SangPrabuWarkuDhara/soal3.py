katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

riwayat_buku = set()
def proses_transaksi(katalog, nama_buku, jumlah_beli):
    
    for i in katalog:
        if nama_buku == i['nama'].lower():
            if i['stok']<=0:
                print("buku ditemukan")
            riwayat_buku.append(i['nama'])

        else:
            print("buku tidak ditemukan")

nama_buku = str(input("masukkan nama buku: "))
jumlah_beli = int(input("masukkan jumlah: "))

#AKU TELAH BERUSAHA BANG ;
