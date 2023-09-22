import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
tmp = 0

if B + C < 60:
    print("{} {}".format(A, B+C))
else:
    tmp = B + C
    A = A + (tmp // 60)
    B = tmp % 60
    if A >= 24:
        A = A - 24
        print("{} {}".format(A, B))
    else: print("{} {}".format(A, B))