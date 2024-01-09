import sys
N = int(sys.stdin.readline()); data = []; result = []
for i in range(N):
    a,b,c = map(int,sys.stdin.readline().split())
    data.append([a,b,c])
for i in range(N):
    if data[i][0] == data[i][1] and data[i][1] == data[i][2] and data[i][0] == data[i][2]:
        result.append(10000 + data[i][0] * 1000)
    elif data[i][0] != data[i][1] and data[i][1] != data[i][2] and data[i][0] != data[i][2]:
        result.append(max(data[i]) * 100)
    else:
        if data[i].count(data[i][0]) == 2:
            result.append(1000 + data[i][0] * 100)
        else:
            result.append(1000 + data[i][1] * 100)
print(max(result))