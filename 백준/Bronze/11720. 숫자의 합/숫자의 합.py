import sys
N = int(sys.stdin.readline())
numbers = sys.stdin.readline().strip(); result = 0
for i in range(len(numbers)): result += int(numbers[i])
print(result)