import sys

T = int(sys.stdin.readline())
sum = []
for i in range(0,T):
    A, B = map(int,sys.stdin.readline().split())
    sum.append(A+B)

for i in range(0,T):
    print("Case #{}: {}".format(i+1,sum[i]))