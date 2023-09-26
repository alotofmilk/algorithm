import sys
T = int(sys.stdin.readline()); data = []; answer = []
for i in range(0,T):
    case = sys.stdin.readline().split()
    data.append(case)

for i in range(0,T):
    answer.append(float(data[i][0]))
    for j in range(1,len(data[i])):
        if data[i][j] == "@":
            answer[i] = answer[i] * 3
        elif data[i][j] == "%":
            answer[i] = answer[i] + 5
        else:
            answer[i] = answer[i] - 7

for i in range(0,len(answer)):
    print("{:.2f}".format(answer[i]))