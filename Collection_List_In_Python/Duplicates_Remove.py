old_list = ["ALi","Kousar","Sky","Surhan","AL  i","Kousar","Pinki"]
new_list = []
for item in old_list:
    if item not in new_list:
        new_list.append(item)
print("New_List is:",new_list)