Credit_number = "1234_5678_9012_3456"
last_degit = Credit_number [::-1]
#last_degit = Credit_number [-4:]
#print(Credit_number[3])
#print(Credit_number[1:3])
#print(Credit_number[5:9])
#print(Credit_number[10:14])
#print(Credit_number[15:19])
#print(Credit_number[-5])
#print(Credit_number[::3]) # we use :: for step
print(f"XXXX_XXXX_XXXX_{last_degit}")
#STring indexing [start:end:step]