class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def _insert_recursive(self, current, new_node):
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None

        if id_buku == current.id:
            return current
        elif id_buku < current.id:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)

    def inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(f"{current.id} - {current.judul}")
            self._inorder_recursive(current.right)

    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # sesuai definisi height edge

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return max(left_height, right_height) + 1


# ==========================
# MAIN PROGRAM
# ==========================
bst = BST()

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# TRAVERSAL
bst.inorder()

# SEARCH
print("\n[SEARCH] Mencari ID 60...")
result = bst.search(60)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")

print("\n[SEARCH] Mencari ID 100...")
result = bst.search(100)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")

min_node = bst.get_min()
max_node = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_node.id}")
print(f"[STATISTIK] ID Terbesar: {max_node.id}")

print(f"\n[INFO] Tinggi (Height) Tree: {bst.height()}")

print("=========================================")
print("Simulasi Selesai!")
