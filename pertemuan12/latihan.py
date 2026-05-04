class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearhTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Langkah 1
        new = Node(data)

        # Langkah 2
        if self.root == None:
            # Jika iya
            self.root = new
            return
        
        # Jika tidak
        # Langkah 3
        P = self.root
        Q = self.root

        #langkah 4
        while Q != None and new.data != P.data:
            #langkah 5
            P = Q

            # Langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        # Langkah 7
        if new.data == P.data:
            # Jika iya
            print("Data duplikat")
            return
            
        # Jika tidak
        # Langkah 8
        if new.data < P.data:
            # Jika iya
            P.left = new
        # Jika tidak
        else:
            P.right = new
        # Selesai

bst = BinarySearhTree()

bst.insert(12)
bst.insert(9)
bst.insert(99)
bst.insert(67)
bst.insert(35)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)

in_order(bst.root)