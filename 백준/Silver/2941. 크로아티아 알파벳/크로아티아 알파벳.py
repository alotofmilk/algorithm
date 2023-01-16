import sys
sentence = sys.stdin.readline();
dictionary = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in dictionary: sentence = sentence.replace(i, "*")
print(len(sentence)-1)