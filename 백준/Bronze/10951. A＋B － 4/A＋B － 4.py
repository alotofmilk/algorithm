import sys

sum = 0
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        sum = A + B
        print(sum)
    except:
        break