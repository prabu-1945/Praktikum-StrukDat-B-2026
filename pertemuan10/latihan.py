#BAGIAN 1
class StackList:
    def __init__(self):
        self.items = []  

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


#BAGIAN 2
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0  

    def is_empty(self):
        return self.top is None

    def push(self, url):
        new_node = Node(url)       
        new_node.next = self.top   
        self.top = new_node        
        self.count += 1            

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        
        removed_url = self.top.url  
        self.top = self.top.next    
        self.count -= 1             
        
        return removed_url          

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count


browser = StackList()
browser.push("google.com")
browser.push("youtube.com")
print(browser.peek())  
print(browser.pop())   
print(browser.size())  


browser2 = StackLinkedList()
browser2.push("github.com")
browser2.push("stackoverflow.com")
print(browser2.peek())  
print(browser2.pop())   
print(browser2.size())  