import sys
sum = 0; number = 0
while number != -1:
    number = int(sys.stdin.readline().strip())
    if number != -1: sum += number
    else: break
print(sum)