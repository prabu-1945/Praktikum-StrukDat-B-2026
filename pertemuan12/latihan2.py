class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node


bst = BinaryTree()

bst.insert_root('f')
bst.insert_left(bst.root, 'b')
bst.insert_right(bst.root, 'g')
bst.insert_left(bst.root.left, 'a')
bst.insert_right(bst.root.left, 'd')
bst.insert_left(bst.root.left.right, 'c')
bst.insert_right(bst.root.left.right, 'e')
bst.insert_right(bst.root.right, 'i')
bst.insert_left(bst.root.right.right, 'h')

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

inorder(bst.root)