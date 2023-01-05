import sys
numbers = [int(sys.stdin.readline().strip()) for i in range(28)]
all_students = [i for i in range(1,31)]
find_students = []
for i in range(0,30):
    if all_students[i] not in numbers:
        find_students.append(all_students[i])
print("{}\n{}".format(find_students[0],find_students[1]))