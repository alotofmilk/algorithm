import sys

N = int(sys.stdin.readline())
X = N // 10
Y = N % 10
x = X
y = Y
sum = 0
new_number = 0
cycle_cnt = 0

if X == 0 and Y == 0:
    cycle_cnt += 1
else:
    while (new_number != 10 * X + Y):
        sum = x + y
        if sum < 10:
            new_number = y * 10 + sum
        else:
            new_number = y * 10 + sum % 10
        cycle_cnt += 1
        x = new_number // 10
        y = new_number % 10

print(cycle_cnt)