import sys
A, B = map(str, sys.stdin.readline().split()); A_sum = 0; B_sum = 0
for i in range(len(A)): A_sum += int(A[i])
for i in range(len(B)): B_sum += int(B[i])
print(A_sum * B_sum)