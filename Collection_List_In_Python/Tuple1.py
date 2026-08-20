#TUPLE : ()  (IMMUTABLE) MEANS PERMANENET ORDERED AND UNCHANGEABLE.DUPLICATE OK .FASTER

my_tuple = ("apple", "banana", "cherry","mango","grape","apple","pineapple")
print(dir(my_tuple))
print(help(my_tuple))
print(len(my_tuple))
print("grape"in my_tuple)
print(my_tuple.index("grape"))
print(my_tuple.count("apple"))
for tuple in my_tuple:
    print(tuple)