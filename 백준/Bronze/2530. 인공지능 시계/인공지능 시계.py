import sys
A, B, C = map(int,sys.stdin.readline().split())
D = int(sys.stdin.readline())
cnt = C + D
if cnt < 60:
    print("{} {} {}".format(A, B, cnt))
else:
    B += cnt // 60
    C = cnt % 60
    if B < 60:
        print("{} {} {}".format(A, B, C))
    else:
        A += B // 60
        B = B % 60
        if A < 24:
            print("{} {} {}".format(A, B, C))
        else:
            A = A % 24
            print("{} {} {}".format(A, B, C))