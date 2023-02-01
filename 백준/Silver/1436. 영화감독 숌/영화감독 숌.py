import sys
N = int(sys.stdin.readline()); number = 666; cnt = 0
while True:
    if "666" in str(number): cnt += 1
    if cnt == N:
        print(number)
        break
    number += 1