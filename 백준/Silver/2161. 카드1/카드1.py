import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque(); numbers = deque()
for i in range(N): queue.append(i+1)
cnt = 1
while len(queue) > 1:
    if cnt % 2 == 1:
        numbers.append(queue.popleft())
        cnt += 1
    elif cnt % 2 == 0:
        tmp = queue.popleft()
        queue.append(tmp)
        cnt += 1
print(*numbers, *queue, sep=" ")