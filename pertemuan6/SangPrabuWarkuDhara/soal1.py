
def tambah_buku(nama, harga, stok):
    if harga < 0 or stok < 0:
        print("error")
        return None
    else:
        return{"nama":nama, "harga":harga, "stok":stok}
    
list_buku = []
i = 0
while i < 3:

    nama = str(input("nama buku:"))
    harga = float(input("harga:"))
    stok = int(input("jumlah stok:"))
    list_buku.append(tambah_buku(nama, harga, stok))
    i += 1
    
    print("list buku")
    for x in list_buku:
        print(x)
