temp = 0
is_sunny = True
if temp>=28 and is_sunny:
    print("today is very hot day")
    print("today sunshine 😎 more:")   # emogi short cut is window + ; or. daba ker emogi aye ga
elif temp<=0 and is_sunny:
    print("today is very cold 😨day")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
elif temp >=28 and not is_sunny:
    print("it is cold outside")
    print("today is cloudy")
