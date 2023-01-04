import sys

T = int(sys.stdin.readline())
num1 = []
num2 = []
sum = []
for i in range(0,T):
    A, B = map(int, sys.stdin.readline().split())
    num1.append(A)
    num2.append(B)
    sum.append(A + B)

for i in range(0,T):
    print("Case #{}: {} + {} = {}".format(i+1,num1[i],num2[i],sum[i]))