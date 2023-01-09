import sys
N = int(sys.stdin.readline())
numbers = sys.stdin.readline(); sum = 0
for i in range(N): sum += int(numbers[i])
print(sum)