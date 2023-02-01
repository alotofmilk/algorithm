import sys
N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split())); result = 0
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] > M: continue
            else: result = max(result, numbers[i] + numbers[j] + numbers[k])
print(result)