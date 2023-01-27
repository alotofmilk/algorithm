import sys
numbers = [int(sys.stdin.readline().strip()) for i in range(10)]
remainder = set([numbers[i] % 42 for i in range(10)])
print(len(remainder))