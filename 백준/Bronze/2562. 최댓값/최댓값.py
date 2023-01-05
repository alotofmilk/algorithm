import sys
numbers = [int(sys.stdin.readline().strip()) for i in range(9)]
find_max = lambda list: print("{}\n{}".format(max(list),list.index(max(list))+1))
find_max(numbers)