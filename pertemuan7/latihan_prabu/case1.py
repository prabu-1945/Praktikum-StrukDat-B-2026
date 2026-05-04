#tugas1
history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    print(history_array)

keyword = input("masukkan keyword: ")

tambah_pencarian_array(keyword)

#tugas2
keyword = input("masukkan keyword: ")
class Node:
    def __init__(self, keyword):
        self.data = keyword
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None
    
    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node

    def tampilkan_history(self):
        curr = self.head
        while curr:
            history_array.append(curr.data)
            curr = curr.next
        print(history_array)

ll=HistoryLinkedList()
ll.tambah_pencarian_linked(keyword)
ll.tampilkan_history()
