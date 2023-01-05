import sys
N = int(sys.stdin.readline())
answer_list = [sys.stdin.readline().strip() for i in range(N)]
cnt = 1
succession = 0
sum = 0
for i in range(0,len(answer_list)):
    for j in range(0,len(answer_list[i])):
        if answer_list[i][j] == "O":
            if succession == 0:
                sum += cnt
                succession += 1
            elif succession > 0:
                cnt += 1
                sum += cnt
                succession += 1
        else:
            succession = 0
            cnt = 1
    print(sum)
    sum = 0
    succession = 0
    cnt = 1