t = input()
T = int(t)

matrix = []
for i in range(0,T):
    a,b = input().split()
    A = int(a)
    B = int(b)
    sum = A + B
    matrix.append(sum)

for i in range(0,T):
    print(matrix[i])