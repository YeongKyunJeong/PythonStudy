# dfs.py

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

# 매개변수 : 그래프, 시작 노드
def my_dfs(graph, start_node):
    # 1 탐색할 노드를 담을 스택
    # stack = []
    stack = list()

    # 2. 방문 여부 확인 리스트
    visited = list()

    # 3. 탐색 시작 노드
    stack.append(start_node)

    # 6. 탐색할 노드가 없을 때까지 4 ~ 5 반복
    while stack:
        # 4. 방문할 노드를 스택에서 꺼냄
        node = stack.pop()

        # 5. 방문 리스트에 스택에서 꺼낸 노드가 없으면,
        if node not in visited:
            # 인접 노드를 스택에 추가
            stack.extend(reversed(graph[node])) # 뒤집어서 넣기
            visited.append(node)

        # if node not in visited:
        #     for node_nxt in graph[node]:
        #         if node_nxt not in visited:
        #             stack.append(node_nxt) # 여러 개를 한꺼번에 추가
    return visited

# print(my_dfs(graph, "A"))

def my_graphdfs(graph, startnode):
    stack = [startnode]
    visited = {startnode}
    order = []

    while stack:
        cur = stack.pop()
        order.append(cur)

        for nxt in reversed(graph[cur]):
            if nxt in visited:
                continue
            stack.append(nxt)
            visited.add(nxt)

    return order

# print( my_graphdfs(graph, "A"))

graph = { "1" : ["2", "3", "4"], 
         "2" : ["1", "5"],
         "3" : ["1", "6"],
         "4" : ["1", "6"],
         "5" : ["2", "6"],
         "6" : ["3", "4", "5"]
         }


def graphdfs(graph, startnode):
    stack = [startnode]
    visited = {startnode}
    order = []

    while stack:
        cur = stack.pop()
        order.append(cur)

        for nxt in reversed(graph[cur]):
            if nxt in visited:
                continue
            stack.append(nxt)
            visited.add(nxt)

    return order

print(graphdfs( graph, "1"))