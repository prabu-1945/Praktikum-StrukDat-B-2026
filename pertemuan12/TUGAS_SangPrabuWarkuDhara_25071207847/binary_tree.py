class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        print("[INFO] Membangun Struktur Gudang...")

        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')

        self.root.left.left = Node('D')
        self.root.left.right = Node('E')

        self.root.right.right = Node('F')

        print("[INFO] Struktur berhasil dibuat.")

    def preorder(self, node):
        if node:
            print(node.data, end=" - ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" - ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" - ")

    def get_leaf_nodes(self, node, leaves):
        if node:
            if node.left is None and node.right is None:
                leaves.append(node.data)
            self.get_leaf_nodes(node.left, leaves)
            self.get_leaf_nodes(node.right, leaves)


# ======================
# MAIN PROGRAM
# ======================
bt = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")

bt.insert_manual()

print("\nHASIL AUDIT:")

print("1. Pre-Order : ", end="")
bt.preorder(bt.root)

print("\n2. In-Order : ", end="")
bt.inorder(bt.root)

print("\n3. Post-Order : ", end="")
bt.postorder(bt.root)

# LEAF NODE
leaves = []
bt.get_leaf_nodes(bt.root, leaves)

print(f"\n[DATA] Gudang Ujung (Leaf Nodes): {', '.join(leaves)}")

print("======================================")
print("Audit Selesai!")
