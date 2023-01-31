import sys
matrix = []; read = ""
for i in range(5):
    line = list(map(str,sys.stdin.readline()))
    if len(line) < 15: line += " " * (15 - len(line))
    matrix.append(line)
for i in range(15):
    for j in range(5): read += matrix[j][i]
result = "".join(read.split())
print(result)