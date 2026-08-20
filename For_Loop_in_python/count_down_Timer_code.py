import time
my_time = int (input("Enter the time in seconds:"))

for x in range(my_time, 0,-1): #(0,my_time) this for direct number print   # reversed lagaeno ahe
 seconds = x % 60
 minute = int(x / 60) % 60
 hours = int(x / 3600)
 print(f"{hours:01}:{minute:01}:{seconds:01} ")

 time.sleep(1)

print(" TIMES UP!")