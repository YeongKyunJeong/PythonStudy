# graph.py

graph = { "A" : ["B", "C", "D"], 
         "B" : ["A", "E"],
         "C" : ["A", "F", "G"],
         "D" : ["A", "H"],
         "E" : ["B", "I"],
         "F" : ["C", "J"],
         "G" : ["C"],
         "H" : ["D"],
         "I" : ["E"],
         "J" : ["F"]
         }

from collections import deque

def my_bfs(graph, startnode):

    stack = deque(startnode)
    visited = {startnode}
    order = []

    while stack :
        cur = stack.popleft()
        order.append(cur)

        for nxt in graph[cur]:
            if nxt in visited:
                continue
            stack.append(nxt)
            visited.add(nxt)

    return order

print( my_bfs(graph, "A"))


