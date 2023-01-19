import sys
dial = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
word = sys.stdin.readline().strip(); count = 0
dial_keys_list = list(dial.keys())
for i in range(len(word)):
    for j in range(len(dial_keys_list)):
        if word[i] in dial_keys_list[j]: count += dial[dial_keys_list[j]]
print(count)