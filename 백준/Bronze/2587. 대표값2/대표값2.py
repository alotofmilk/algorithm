import sys
numbers = [int(sys.stdin.readline().strip()) for i in range(5)]
print(int(sum(numbers) / len(numbers)))
print(sorted(numbers)[2])