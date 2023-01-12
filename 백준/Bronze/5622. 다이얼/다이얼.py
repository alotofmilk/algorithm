import sys
code = sys.stdin.readline()

telephone = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]; get_number = 0; time = 0
for i in range(len(code)):
    for j in range(len(telephone)):
        if code[i] in telephone[j]:
            get_number = j + 2
            time += get_number + 1
            get_number = 0
print(time)