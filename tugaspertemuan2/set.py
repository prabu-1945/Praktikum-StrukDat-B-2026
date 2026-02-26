'''
Set adalah koleksi yang tidak terurut, tidak dapat diubah, dan tidak terindeks, serta tidak 
mengizinkan nilai duplikat. Set ditulis dengan tanda kurung kurawal.
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, False, 0, 1, 2}

thisset = set(("apple", "banana", "cherry")) 
print(thisset)
#Set dapat dibuat dengan menggunakan konstruktor set().
thisset = {"apple", "banana", "cherry"}


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "watermelon"]
thisset.update(tropical)
thisset.update(mylist)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = (1, 2, 3)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2) 
print(set1)
#update berfungsi untuk menyisipkan semua item dari satu set ke set lainnya.
#Union dan update akan mengecualikan item duplikat apapun.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)