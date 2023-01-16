import sys
N = int(sys.stdin.readline()); answer = []; zero = 0; one = 0;
for i in range(N):
    answer.append(int(sys.stdin.readline()))
    if answer[i] == 0: zero += 1
    elif answer[i] == 1: one += 1
if zero > one: print("Junhee is not cute!")
elif one > zero: print("Junhee is cute!")