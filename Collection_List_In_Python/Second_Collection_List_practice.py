#LIST :[] ORDERED AND(MUTABLE)MEANS CHANGEABLE.DUPLICATES OK.

fruits = ["apple", "banana","apple", "cherry"]
fruits.append("mango")
fruits.remove("apple")
fruits.insert(0, "apple")
fruits.sort()
#fruits.reverse()
#fruits.clear()
print(fruits.index("mango"))
print(fruits.count("apple"))
fruits.pop()
print(fruits)