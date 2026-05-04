class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong!")
            return None

        pasien = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {pasien.nama} (keluhan: {pasien.keluhan})")
        return pasien

    def peek(self):
        if self.is_empty():
            print("Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def tampilkan(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f"  {no}. {current.nama.upper()} → {current.keluhan}")
            current = current.next
            no += 1

print("====================================")
print("  SISTEM ANTRIAN POLI UMUM")
print("  RS Sehat Bersama")
print("====================================")

antrian = Queue()

print(f"[CEK] Apakah antrian kosong? → {'YA, antrian masih kosong.' if antrian.is_empty() else 'TIDAK'}")

antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")

print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

antrian.peek()
antrian.dequeue()
antrian.enqueue("Dodi", "nyeri perut")
antrian.tampilkan()
antrian.dequeue()
print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
antrian.clear()

print(f"[CEK] Apakah antrian kosong? → {'YA, antrian sudah kosong.' if antrian.is_empty() else 'TIDAK'}")

print("====================================")
print("  Simulasi Selesai!")
print("====================================")