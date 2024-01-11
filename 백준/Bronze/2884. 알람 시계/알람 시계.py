import sys
H, M = map(int,sys.stdin.readline().split())
if M - 45 >= 0:
    print("{} {}".format(H, M-45))
else:
    if H > 0:
        H = H - 1
        M = M + 60 - 45
        print("{} {}".format(H, M))
    else:
        H = 23
        M = M + 60 - 45
        print("{} {}".format(H, M))