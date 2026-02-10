thislist = ["apple", "banana", "cherry", "apple", "cherry"] 
print(thislist) 

thislist = ["apple", "banana", "cherry"] 
print(thislist[-1]) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[2:5]) 

list1 = ["abc", 34, True, 40, "male"] 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[:4]) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[2:]) 

thislist = ["apple", "banana", "cherry"] 
if "apple" in thislist: 
    print("Yes, 'apple' is in the fruits list") 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"] 
thislist[1:3] = ["blackcurrant", "watermelon"] 
print(thislist) 

thislist = ["apple", "banana", "cherry"] 

thislist.insert(2, "watermelon") 
print(thislist) 

thislist = ["apple", "banana", "cherry"] 

thislist.append("orange") 
print(thislist) 

thislist = ["apple", "banana", "cherry"] 
tropical = ["mango", "pineapple", "papaya"] 
thislist.extend(tropical) 
print(thislist) 

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list3)