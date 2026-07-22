# Simulation.py

dirs = [
    [0, 1],
    [-1, 0], 
    [0, -1],
    [1, 0]
]

def cctv_problem_01(n, m, grid):
    
    empty_count = 0
    cctvs = []

    for r in range(n):
        for c in range(m):
            
            if grid[r][c] == 0:
                empty_count += 1

            elif grid[r][c] == 2:
                cctvs.append((r,c))

    answer = empty_count
    K = len(cctvs)

    def scan_direction(r, c, idx_dir):

        dr, dc = dirs[idx_dir]

        nr = r + dr
        nc = c + dc

        watched_cells = []

        while 0 <= nr < n and 0 <= nc < m:

            if grid[nr][nc] == 1:
                break

            if grid[nr][nc] == 0:
                watched_cells.append((nr, nc))

            nr += dr
            nc += dc

        return watched_cells
    
    covermap = [[0]*m for _ in range(n)]

    def dfs(idx_cctv, watched_count):

        nonlocal answer

        if idx_cctv == K:
            answer = min(answer, empty_count - watched_count)
            return
        
        for idx_dir in range(4):
            watched_thistime = 0
            r, c = cctvs[idx_cctv]
            watched_cells = scan_direction(r, c, idx_dir)

            for ir, ic in watched_cells:
                
                if covermap[ir][ic] == 0:
                    watched_thistime += 1

                covermap[ir][ic] += 1
                
            dfs(idx_cctv + 1, watched_count + watched_thistime)

            for ir, ic in watched_cells:

                covermap[ir][ic] -= 1 
    
    dfs(0, 0)

    return answer

print(cctv_problem_01(3, 5, [
    [0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0],
    [0, 0, 0, 0, 0]    
]))

print(cctv_problem_01(5, 6, [
    [0, 0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0]    
]))

print(cctv_problem_01(8, 8, [
    [0, 0, 0, 0, 0, 0, 1, 2],
    [0, 2, 0, 1, 0, 0, 2, 2],
    [0, 0, 0, 0, 2, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 2, 0, 0], 
    [0, 1, 0, 2, 0, 2, 0, 0],
    [2, 0, 1, 0, 0, 1, 0, 0]  
]))



# def cctv_problem_02(n, m, grid):

#     dirs = [
#         [0, 1],
#         [-1, 0], 
#         [0, -1],
#         [1, 0]
#     ]

#     cctvs = []
#     empty_count = 0
    
#     for r in range(n):
#         for c in range(m):
            
#             if grid[r][c] == 2:
#                 cctvs.append((r, c))

#             elif grid[r][c] == 0:
#                 empty_count += 1

#     answer = empty_count

#     def watch(r, c, idx_dir):

#         watched_room = []

#         dr = dirs[idx_dir][0]
#         dc = dirs[idx_dir][1]

#         nr = r + dr
#         nc = c + dc

#         while 0 <= nr < n and 0 <= nc < m:

#             if grid[nr][nc] == 1:
#                 break

#             if grid[nr][nc] == 0:
#                 watched_room.append((nr, nc))

#             nr += dr
#             nc += dc

#         return watched_room
    
#     covermap = [[0]*m for _ in range(n)]

#     def dfs(idx_cctv, watch_count):

#         nonlocal answer

#         if idx_cctv == len(cctvs):
#             answer = min(answer, empty_count - watch_count)

#             return
        
#         r = cctvs[idx_cctv][0]
#         c = cctvs[idx_cctv][1]

#         for idx_dir in range(4):

#             watched_room = watch(r, c, idx_dir)
#             watched_thistime = 0

#             for wr, wc in watched_room:

#                 if covermap[wr][wc] == 0:
#                     watched_thistime += 1

#                 covermap[wr][wc] += 1

#             dfs(idx_cctv + 1, watch_count + watched_thistime)


#             for wr, wc in watched_room:
#                 covermap[wr][wc] -= 1

#     dfs(0, 0)

#     return answer

# print(cctv_problem_02(3, 5, [
#     [0, 0, 0, 0, 0],
#     [0, 2, 0, 1, 0],
#     [0, 0, 0, 0, 0]    
# ]))

# print(cctv_problem_02(5, 6, [
#     [0, 0, 0, 0, 0, 0],
#     [0, 2, 0, 1, 0, 0],
#     [0, 0, 0, 0, 2, 0],
#     [0, 0, 0, 0, 0, 0], 
#     [1, 0, 0, 0, 0, 0]    
# ]))


    
    








