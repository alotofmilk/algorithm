import sys
sentence = sys.stdin.readline().strip(); flag = 0
if len(sentence) % 2 == 1:
    for i in range(0, (len(sentence) + 1) // 2):
        if sentence[i] == sentence[len(sentence)-1-i]: pass
        else: flag = 1
    if flag == 0: print(1)
    else: print(0)
else:
    for i in range(len(sentence) // 2):
        if sentence[i] == sentence[len(sentence)-1-i]: pass
        else: flag = 1
    if flag == 0: print(1)
    else: print(0)