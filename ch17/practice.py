# practice.py

maze = [[0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        ]

maze = [[0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        ]

maze1 = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
]


from collections import deque
dirs = ([0, 1], [-1, 0], [0, -1], [1, 0])

def solve_maze_bfs(maze, start):
    n = len(maze)
    queue = deque()
    queue.append(start)
    visited = [[False]*n for _ in range(n)]
    visited[start[0]][start[1]] = True
    order = []
    depth = 0
    while queue:
        curi, curj = queue.pop()
        order.append((curi, curj))

        for dir in dirs:
            nxti = curi + dir[0]
            nxtj = curj + dir[1]
            if (nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= n 
                or visited[nxti][nxtj] 
                or maze[nxti][nxtj] == 1):
                continue
            queue.append((nxti, nxtj))
            visited[nxti][nxtj] = True

        depth += 1

    return order, depth
print(solve_maze_bfs(maze1, [0, 0]))

dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
def solve_maze_dfs(graph, start):
    n = len(graph)
    stack = [start]
    visited = [[False]*n for _ in range(n)]
    visited[start[0]][start[1]] = True
    order = []

    while stack:
        curi, curj = stack.pop()
        order.append((curi, curj))

        for dir in dirs:
            nxti = curi + dir[0]
            nxtj = curj + dir[1]

            if (nxti < 0 or nxti >= n 
                or nxtj < 0 or nxtj >= n
                or visited[nxti][nxtj]
                or graph[nxti][nxtj] == 1):
                continue

            stack.append((nxti, nxtj))
            visited[nxti][nxtj] = True

    return order

print(solve_maze_dfs(maze, (0, 0)))
print(solve_maze_dfs(maze1, [0, 0]))

def solve_maze(maze, start):
    stack = list(start)
    visited = ()
    n = len(maze)
    while stack:
        r, c = stack.pop()

        if (r, c) not in visited:
            visited.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr 
                nc = c + dc

                if (0 <= nr < n and 0 <= nc < c 
                    and maze[nr][nc] == 0):
                    stack.append((nr, nc))

                    