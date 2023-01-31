import sys
N, M = map(int,sys.stdin.readline().split())
A_matrix = []; B_matrix = []; result = []
for i in range(2*N):
    line = list(map(int,sys.stdin.readline().split()))
    if len(A_matrix) < N: A_matrix.append(line)
    else: B_matrix.append(line)

for i in range(N):
    result.append([])
    for j in range(M):
        result[i].append(A_matrix[i][j] + B_matrix[i][j])
        print(result[i][j], sep = " ", end = " ")
    print()