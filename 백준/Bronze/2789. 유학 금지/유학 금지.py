import sys
sentence = sys.stdin.readline(); new_sentence = ""
check = ["C","A","M","B","R","I","D","G","E"]
for i in range(len(sentence)):
    if sentence[i] not in check: new_sentence += sentence[i]
    elif sentence[i] in check: pass
print(new_sentence)