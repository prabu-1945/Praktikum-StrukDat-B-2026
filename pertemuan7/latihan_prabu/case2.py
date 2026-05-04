#tugas1
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

nama_pasien = input("masukkan nama pasien: ")
posisi = int(input("masukkan posisi: "))

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi-1, nama_pasien)

sisipkan_pasien_darurat_array(nama_pasien, posisi)
print(f"antrian saat ini: {antrean_array}")

#tugas2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, nama_pasien, posisi):
        new_node = Node(nama_pasien)
        
        if posisi <= 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
       
        while current.next is not None and count < posisi - 1:
            current = current.next
            count += 1
      
        new_node.next = current.next
        current.next = new_node

    def tampilkan(self):
        curr = self.head
        if not curr:
            print("Antrean kosong.")
            return
        
        while curr:
            antrean_array.append(curr.data)
            curr = curr.next
        print(antrean_array)

antrean = AntreanLinkedList()

nama_pasien = input("\nMasukkan nama pasien: ")
possi = int(input("Masukkan posisi: "))

antrean.insert_at_position(nama_pasien, posisi)
print("\nantrian saat ini")
antrean.tampilkan()