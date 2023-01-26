import sys
T = int(sys.stdin.readline())
money = []; quarter = 0; dime = 0; nickel = 0; penny = 0
for i in range(T):
    money.append(int(sys.stdin.readline().strip()))
    quarter = money[i] // 25
    dime = (money[i] % 25) // 10
    nickel = ((money[i] % 25) % 10) // 5
    penny = (((money[i] % 25) % 10) % 5) // 1
    print("{} {} {} {}".format(quarter,dime,nickel,penny))