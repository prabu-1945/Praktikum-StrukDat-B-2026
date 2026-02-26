angka = [10, 20, 30, 40, 50]
total = 0
#tambahkan 60
angka.append(60)
#hapus angka 20
angka.remove(20)

print(max(angka))
print(min(angka))

for n in angka:
    total += n
avg = total / len(angka)
print(f"avg: {avg}")