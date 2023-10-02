import sys
S = int(sys.stdin.readline())
answer = []; cnt = 1
while True:
    S = S - cnt
    if S < 0: break
    else:
        answer.append(cnt)
        cnt = cnt + 1
print(len(answer))