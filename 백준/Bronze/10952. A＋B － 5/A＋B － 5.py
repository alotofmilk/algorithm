import sys

A = int(1)
B = int(1)
sum = []
while not(A == 0 and B == 0):
    A, B = map(int, (sys.stdin.readline().split()))
    sum.append(A+B)

for i in range(0,len(sum)):
    if sum[i] != 0:
        print(sum[i])
    else:
        break