dictionary1 = {"milk":160,"oil":460,"rice":220,"sugar":370,"Biryani packet":90}
dictionary2 = {"tomato":480,"chilly":400,"milk":260,"rice":550,"Biryani packet":110}
total = dictionary1.copy()
for item, qnt in dictionary2.items():
    if item in total:
        total[item] = total[item] + qnt
    else:
        total[item] = qnt
print(total)


