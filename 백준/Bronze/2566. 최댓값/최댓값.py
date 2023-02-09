import sys
matrix = [list(map(int,sys.stdin.readline().split())) for i in range(9)]
result = 0; position = [0,0]
for i in range(9):
    for j in range(9):
        if result <= matrix[i][j]:
            result = matrix[i][j]
            position[0] = i+1
            position[1] = j+1
print(result)
print(*position)