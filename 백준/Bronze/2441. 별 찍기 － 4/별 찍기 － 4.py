import sys
N = int(sys.stdin.readline().strip()); star = "*" * N
for i in range(0,N):
    print(star)
    star = " " + star[:-1]