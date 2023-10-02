import sys
T = int(sys.stdin.readline()); case = []; answer = []; tmp1 = 0; tmp2 = 0
for i in range(T):
    A, B = map(int,sys.stdin.readline().split())
    case.append([A,B])
    answer.append(1)
for i in range(T):
    if case[i][0] == 1 and case[i][1] != 1:
        answer[i] = case[i][1]
    elif case[i][1] == 1 and case[i][0] != 1:
        answer[i] = case[i][0]
    elif case[i][0] == case[i][1]:
        answer[i] = case[i][0]
    else:
        if case[i][0] < case[i][1]:
            tmp1 = case[i][0]; tmp2 = case[i][1]
            for j in range(2,case[i][0]+1):
                while True:
                    if tmp1 % j == 0 and tmp2 % j == 0:
                        tmp1 = tmp1 // j
                        tmp2 = tmp2 // j
                        answer[i] = answer[i] * j
                    else:
                        break
            answer[i] = answer[i] * (case[i][0] // answer[i]) * (case[i][1] // answer[i])
        elif case[i][0] > case[i][1]:
            tmp1 = case[i][1]; tmp2 = case[i][0]
            for j in range(2,case[i][1]+1):
                while True:
                    if tmp1 % j == 0 and tmp2 % j == 0:
                        tmp1 = tmp1 // j
                        tmp2 = tmp2 // j
                        answer[i] = answer[i] * j
                    else:
                        break
            answer[i] = answer[i] * (case[i][0] // answer[i]) * (case[i][1] // answer[i])
    print(answer[i])