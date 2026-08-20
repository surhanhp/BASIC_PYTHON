words = ["python", "java","python", "java","cpp", "go","cpp","java", "javascript"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(f" word is present{count}")