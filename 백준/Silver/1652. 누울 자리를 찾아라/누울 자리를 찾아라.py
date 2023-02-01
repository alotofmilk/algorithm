import sys
N = int(sys.stdin.readline().strip())
room = []; width_cnt = 0; height_cnt = 0
for i in range(N): room.append(list(sys.stdin.readline().strip()))
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == ".": cnt += 1
        else: cnt = 0
        if cnt == 2: width_cnt += 1

for j in range(N):
    cnt = 0
    for i in range(N):
        if room[i][j] == ".": cnt += 1
        else: cnt = 0
        if cnt == 2: height_cnt += 1

print(width_cnt, height_cnt, sep = " ")