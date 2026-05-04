#tugas1
history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    print(history_array)

keyword = input("search : ")
    
tambah_pencarian_array(keyword)

#tugas2
class Node:
    def __init__(self, keyword):
    self.data = keyword
    self.next = None

class AntreanLinkedList:
    def __init__(self, keyword):
    self.head = keyword
    self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
    print("null")