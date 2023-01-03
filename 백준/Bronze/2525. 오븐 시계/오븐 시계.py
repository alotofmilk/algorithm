a, b = input().split()
cook = input()

A = int(a)
B = int(b)
cooking_time = int(cook)

if B + cooking_time < 60:
    print("{} {}".format(A, B + cooking_time))
elif B + cooking_time >= 60:
    if A + ((B + cooking_time) // 60) >= 24:
        A = (A + ((B + cooking_time) // 60)) - 24
        B = (B + cooking_time) % 60
        print("{} {}".format(A, B))
    elif A + ((B + cooking_time) // 60) < 24:
        A = (A + ((B + cooking_time) // 60))
        B = (B + cooking_time) % 60
        print("{} {}".format(A, B))