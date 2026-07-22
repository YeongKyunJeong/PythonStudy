# Floyd_Warshall.py

# def solution(n, edges):
    
#     INF = 20000000
#     dist = [[INF] * (n+1) for _ in range(n+1) ]
#     nxt = [[-1] * (n+1) for _ in range(n+1)]

#     for i in range(1, n+1):
#         dist[i][i] = 0
#         nxt[i][i] = i

#     for u, v, cost in edges:
#         if cost < dist[u][v]:
#             dist[u][v] = cost 
#             nxt[u][v] = v
    
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 if dist[i][j] > dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#                     nxt[i][j] = nxt[i][k]
    
#     for i in range(0, n+1):
#         for j in range(0, n+1):
#             if dist[i][j] == INF:
#                 dist[i][j] = -1

#     return dist, nxt

# def restore_path(u, v, nxt):
#     if nxt[u][v] == -1:
#         return [u]
    
#     path = [u]
    
#     while u != v:
#         u = nxt[u][v]
#         path.append(u)

#     return path  

# n = 4
# edges = [
#     [1, 2, 4],
#     [1, 3, 2],
#     [3, 2, 1],
#     [2, 4, 3],
#     [3, 4, 8],
# ]

# dist, nxt = solution(n, edges)
# print(dist)
# print(dist[1][4])
# print(restore_path(1, 4, nxt))

def floyd_warshall(n, edges):

    INF = 2000000
    
    costs = [[INF]*(n + 1) for _ in range(n+1)]
    nxts = [[-1]*(n + 1) for _ in range(n+1)]

    for i in range(1, n + 1):
        costs[i][i] = 0
        nxts[i][i] = i

    for u, v, cost in edges:
        if cost >= costs[u][v]:
            continue

        costs[u][v] = cost
        costs[v][u] = cost
        nxts[u][v] = v
        nxts[v][u] = u

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if costs[i][j] <= costs[i][k] + costs[k][j]:
                    continue

                costs[i][j] = costs[i][k] + costs[k][j]
                costs[j][i] = costs[i][k] + costs[k][j]
                nxts[i][j] = nxts[i][k]
                nxts[j][i] = nxts[j][k]

    for i in range(n + 1):
        for j in range(n + 1):
            if costs[i][j] == INF:
                costs[i][j] = -1

    return costs, nxts

def restore_path(start, end, nxts):
    if start == end:
        return [start]
    
    if nxts[start] == -1:
        return [-1]
    
    path = [start]

    while start != end:
        start = nxts[start][end]
        path.append(start)

    return path

n = 6

edges = [
    [1, 2, 7],
    [1, 3, 9],
    [1, 6, 14],
    [2, 3, 10],
    [2, 4, 15],
    [3, 4, 11],
    [3, 6, 2],
    [4, 5, 6],
    [5, 6, 9],
]

costs, nxts = floyd_warshall(n, edges)

print(costs)
print(edges)
