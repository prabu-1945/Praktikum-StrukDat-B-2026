kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

mata_kuliah_bersama = kelas_A & kelas_B
print("Mata kuliah yang diambil oleh kdua kelas:")
print(mata_kuliah_bersama)

hanya_kelas_A = kelas_A - kelas_B
print("Mata kuliah yang hanya diambil kelas A:")
print(hanya_kelas_A)

semua_mata_kuliah = kelas_A | kelas_B
print("Seluruh mata kuliah UNIK (A dan B):")
print(semua_mata_kuliah)