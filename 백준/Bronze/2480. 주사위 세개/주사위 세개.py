a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)

find_max = 0
find_max_list = [A,B,C]

if A == B and B == C:
    print(10000 + A * 1000)
elif A == B and B != C:
    print(1000 + A * 100)
elif B == C and B != A:
    print(1000 + B * 100)
elif A == C and C != B:
    print(1000 + C * 100)
elif A != B and B != C and C != A:
    for i in range(0,3):
        if find_max_list[i] > find_max:
            find_max = find_max_list[i]
    print(find_max * 100)