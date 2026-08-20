#COLLECTION : SINGLE "VARIABLE" USED TO STORE MULTIPLES VALUES.
#LIST :[] ORDERED AND(MUTABLE)MEANS CHANGEABLE.DUPLICATES OK.

fruits = ["apple", "banana", "cherry"]
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)
print("mango" in fruits)
fruits[0] = "mango"
for fruit in fruits:
 print(fruit)
#print(fruits)
#print(fruits[::-2])
#for x in fruits:
  #  print(x)
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)
