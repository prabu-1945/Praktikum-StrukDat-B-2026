'''
Tuple Adalah Kumpulan data yang terurut dan tidak dapat diubah. Tuple ditulis dengan tanda 
kurung.
'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)
print(type(thistuple))
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

y.append("orange")
thistuple = tuple(y)
print(thistuple)

y.remove("apple")
thistuple = tuple(y)
print(thistuple)

del thistuple

#Del digunakan untuk menghapus tuple.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print(thistuple[i])
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#Kita dapat mengalikan item-item didalam tuple sebanyak yang kita mau.