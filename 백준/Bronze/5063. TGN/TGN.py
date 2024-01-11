import sys
N = int(sys.stdin.readline()); result = []
for i in range(N):
    r, e, c = map(int, sys.stdin.readline().split())
    if e - r > c : result.append("advertise")
    elif e - r == c : result.append("does not matter")
    else: result.append("do not advertise")
print(*result, sep="\n")