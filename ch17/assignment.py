# assignment.py

maze = [[0, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0 ,0 ,0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0]]
# for row in maze:
#     print(row)

# raw = "0 1 1 1 1 1 0 1 0 0 0 10 1 0 1 0 10 1 0 1 0 00 0 0 1 1 01 1 1 1 1 0"

# def makemaze(n, m, rawmaze):
#     maze = [[0] * m for _ in range(n)]
#     rawmaze = ''.join(rawmaze.strip().split())
#     for i in range(n):
#         for j in range(m):
#             if rawmaze[i * m + j] == '1':
#                 maze[i][j] = 1

#     return maze

# print(makemaze(6, 6, raw))


# def explore_maze(maze, start):
#     n = len(maze)
#     m = len(maze[0])
#     stack = [start]
#     visited = []
#     # visited = [[False] * m for _ in range(n) ]
#     # visited[start[0]][start[1]] = True
    
def explore_maze(maze, start):
    n = len(maze)
    m = len(maze[0])
    stack = [start]
    visited = []
    while stack:
        curi, curj = stack.pop()
        if (curi, curj) in visited:
            continue
        visited.append((curi, curj))
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nxti = curi + di
            nxtj = curj + dj
            if (nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= m 
               or (nxti, nxtj) in visited or maze[nxti][nxtj] == 1):
                continue
            stack.append((nxti, nxtj))
    return visited

def explore_maze(maze, start):
    n = len(maze)
    m = len(maze[0])
    stack = [start]
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    order = []
    while stack:
        curi, curj = stack.pop()
        order.append((curi, curj))
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nxti = curi + di
            nxtj = curj + dj
            if (nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= m
                or visited[nxti][nxtj] or maze[nxti][nxtj] == 1):
                continue
            stack.append((nxti, nxtj))
            visited[nxti][nxtj] = True

    return order
        
# print(explore_maze( maze, (0, 0)))
maze = [[0, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0 ,0 ,0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0]]

def explore_maze_bfs(maze, start):
    n = len(maze)
    m = len(maze[0])
    queue = [start]
    visited = []
    while queue:
        curi, curj = queue.pop(0)
        if (curi, curj) in visited:
            continue
        visited.append((curi, curj))
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nxti = curi + di
            nxtj = curj + dj
            if (nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= m
              or maze[nxti][nxtj] == 1):
                continue
            queue.append((nxti, nxtj))
    return visited

print(explore_maze_bfs( maze, (0, 0)))
from collections import deque
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
def explore_maze_bfs(maze, start):
    n = len(maze)
    m = len(maze[0])
    queue = deque()
    queue.append(start)
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    order = []
    while queue:
        curi, curj = queue.popleft()
        order.append((curi, curj))
        for di, dj in dirs:
            nxti = curi + di
            nxtj = curj + dj
            if (nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= m
                or visited[nxti][nxtj] or maze[nxti][nxtj] == 1):
                continue
            queue.append((nxti, nxtj))
            visited[nxti][nxtj] = True
    return order


print(explore_maze_bfs( maze, (0, 0)))