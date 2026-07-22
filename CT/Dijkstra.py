# # Dijkstra.py

import heapq

def dijkstra(n, start, edges):
    
    INF = 2000000
    
    graph = [[] for _ in range(n+1)]
    costs = [INF]*(n + 1)
    costs[start] = 0
    prev = [-1]*(n + 1)
    prev[start] = start

    for u, v, cost in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:

        cur_cost, cur_node = heapq.heappop(pq)
        
        if cur_cost > costs[cur_node]:
            continue
        
        for edge_cost, nxt_node in graph[cur_node]:

            nxt_cost = cur_cost + edge_cost

            if nxt_cost >= costs[nxt_node]:
                continue

            costs[nxt_node] = nxt_cost
            prev[nxt_node] = cur_node
            heapq.heappush(pq, (nxt_cost, nxt_node))

    for i in range(n + 1):
        if costs[i] == INF:
            costs[i] = -1

    return costs, prev

def restore_path(start, end, prev):
    
    if prev[end] == -1:
        return [-1]
    
    path = []
    cur = end

    while cur != start:
        
        path.append(cur)
        cur = prev[cur]

    path.append(start)

    path.reverse()

    return path

n = 8
start = 1

edges = [
    [1, 2, 4],
    [1, 3, 2],
    [2, 3, 1],
    [2, 4, 5],
    [3, 4, 8],
    [3, 5, 10],
    [4, 5, 2],
    [4, 6, 6],
    [5, 6, 2],
    [6, 7, 1],
    [5, 7, 5],
]

costs, prev = dijkstra(n, start, edges)

print(costs)
print(prev)
print(restore_path(start, 1, prev))
print(restore_path(start, 2, prev))
print(restore_path(start, 4, prev))
print(restore_path(start, 7, prev))
print(restore_path(start, 8, prev))
