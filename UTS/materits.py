def hitung_skor(benar, salah):
    poin = (benar * 10) - (salah * 5)

    if poin < 0:
        return 0
    return poin

def mainkan_game(nama_pemain):
    print(f"halo {nama_pemain} selamat bermain")

    jawaban_benar = int(input("masukkan jawaban benar: "))
    jawaban_salah = int(input("masukkan jawaban salah: "))

    total_skor = hitung_skor(jawaban_benar, jawaban_salah)

    return [nama_pemain, total_skor]

def tampilkan_leaderboard(data_skor):
    if not data_skor:
        print("data kosong")
        return

    print('\n'+'='*25)    
    print(f"{'rank':<5} {'nama':<12} {'skor':<5}")
    print('-'*25)

    peringkat = 1
    for baris in data_skor:
        nama = baris[0]
        skor = baris[1]
        print(f"{peringkat:<5} {nama:<12} {skor:<5}")
        peringkat += 1

    print('\n'+'='*25)

def urutkan_descending(data_asli):
    data_copy = []
    for item in data_asli:
        data_copy.append(item[:])

    n = len(data_copy)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data_copy[j][1] > data_copy[max_idx][1]:
                max_idx = j

        data_copy[i], data_copy[max_idx] = data_copy[max_idx], data_copy[i]

    return data_copy

def main():
    database_pemain = []

    while True:
        nama = input("masukkan nama: ")
        if nama.lower() == "selesai":
            break

        hasil_pemain = mainkan_game(nama)
        database_pemain.append(hasil_pemain)

    if database_pemain:
        print("proses")

        leaderboard_terurut = urutkan_descending(database_pemain)
        tampilkan_leaderboard(leaderboard_terurut)
    else:
        tampilkan_leaderboard([])

if __name__ == '__main__':
    main()