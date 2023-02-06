import sys
numbers = int(sys.stdin.readline())
networks = int(sys.stdin.readline())
computer_graph = [[] for i in range(numbers+1)]
for i in range(networks):
    com1, com2 = map(int,sys.stdin.readline().split())
    computer_graph[com1].append(com2)
    computer_graph[com2].append(com1)
visited = [False] * (numbers + 1); start = 1; stack = [start]
while stack:
    cur = stack.pop()
    for adj in computer_graph[cur]:
        if visited[adj] == False:
            visited[adj] = True
            stack.append(adj)
print(visited.count(True)-1)