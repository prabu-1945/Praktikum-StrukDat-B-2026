thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {"colors": ["red", "white", "blue"]}
print(thisdict)

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict.get("model"))
print(list(thisdict.keys()))
print(list(thisdict.values()))
print(list(thisdict.items()))

thisdict["year"] = 2018
print(thisdict)
thisdict.update({"brand": "lamborgini"})
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 2018}
thisdict["color"] = "red"
thisdict.update({"year": 2000})
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["year"]
print(thisdict)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x, y)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()  # ini akan mengcopy data dari thisdict ke mydict
print(mydict)
mydict = dict(thisdict)  # ini akan menyalin data dari thisdict ke mydict
print(mydict)

myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print(myfamily)

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])