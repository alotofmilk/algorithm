year = input()
year = int(year)

if year % 4 == 0:
    if year % 100 != 0:
        print("1")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("1")
        elif year % 400 != 0:
            print("0")
elif year % 4 != 0:
    print("0")