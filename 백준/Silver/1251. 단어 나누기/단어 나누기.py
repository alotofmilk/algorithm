import sys
from itertools import combinations
word = sys.stdin.readline().strip()
iterator = [i for i in range(1,len(word))]
case = list(combinations(iterator,2))
new_word_list = []; new_word_1 = ""; new_word_2 = ""; new_word_3 = ""
for i in range(len(case)):
    new_word_1 = "".join(reversed(word[0:case[i][0]]))
    new_word_2 = "".join(reversed(word[case[i][0]:case[i][1]]))
    new_word_3 = "".join(reversed(word[case[i][1]:]))
    new_word = new_word_1 + new_word_2 + new_word_3
    new_word_list.append(new_word)
new_word_list = sorted(new_word_list)
print(new_word_list[0])