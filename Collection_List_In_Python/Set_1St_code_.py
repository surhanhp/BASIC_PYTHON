#SET : {} UNORDERED AND IMMUTABLE,BUT ADD/REMOVE OK ,NO DUPLICATE.

my_set ={"orange","grapes","apple", "banana", "cherry","banana","apple"}
#print(dir(my_set))
#print(help(my_set))
print(len(my_set))
print("pineapple" in my_set)
my_set.add("pineapple")
my_set.remove("apple")
my_set.pop()
#print(my_set.count("banana"))
#print(my_set.index("orange"))
#my_set.clear()
for my_set in my_set:
    print(my_set)