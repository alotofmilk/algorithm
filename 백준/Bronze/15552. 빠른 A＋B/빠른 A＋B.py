import sys

T = int(sys.stdin.readline())
sum = []
for i in range(0,T):
    a, b = map(int,sys.stdin.readline().split())
    sum.append(a + b)

for i in range(0,T):
    print(sum[i])