import sys
S = sys.stdin.readline().strip(); numbers = S.split(","); sum_numbers = 0
for i in range(len(numbers)): sum_numbers += int(numbers[i])
print(sum_numbers)