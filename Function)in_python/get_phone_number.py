def get_phone_number(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone_number(country=1,area=123,first=456,last=7890)
print(phone_num)