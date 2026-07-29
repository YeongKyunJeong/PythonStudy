# bfs.py

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
    queue = [startnode]
    visited = []

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        queue.extend(graph[node])
        visited.append(node)

    return visited

print(my_bfs(graph, "A"))

def my_graphbfs(graph, startnode):

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

print( my_graphbfs(graph, "A"))

graph = { "1" : ["2", "3", "4"], 
         "2" : ["1", "5"],
         "3" : ["1", "6"],
         "4" : ["1", "6"],
         "5" : ["2", "6"],
         "6" : ["3", "4", "5"]
         }

from collections import deque
def graphbfs(graph, startnode):
    dq = deque(startnode)
    visited = {startnode}
    order = []

    while dq:
        cur = dq.popleft()
        order.append(cur)

        for nxt in graph[cur]:
            if nxt in visited:
                continue
            dq.append(nxt)
            visited.add(nxt)

    return order

print(graphbfs( graph, "1"))
        