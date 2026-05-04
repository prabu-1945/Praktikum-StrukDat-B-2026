katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

def cari_buku(katalog, keyword):

    list = []
    
    for i in katalog:
        if keyword.find(i['nama'].lower()):
            print("buku ditemukan")
            list.append(i['nama'])

        else:
            print("buku tidak ditemukan")

        return list

keyword = str(input("masukkan buku: "))
print(cari_buku(katalog, keyword))