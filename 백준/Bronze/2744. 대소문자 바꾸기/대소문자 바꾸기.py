import sys
sentence = sys.stdin.readline(); answer = ""
for i in range(len(sentence)):
    if ord(sentence[i]) >= 97: answer += sentence[i].upper()
    else: answer += sentence[i].lower()
print(answer)