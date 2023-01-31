import sys
from collections import Counter
numbers = [int(sys.stdin.readline().strip()) for i in range(10)]
average = sum(numbers) // 10
mode_value = max(Counter(numbers).values())
for i,j in Counter(numbers).items():
    if j == mode_value: print(average, i, sep = " ")