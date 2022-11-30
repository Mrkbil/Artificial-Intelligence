class node:
    def __init__(self, vertex, adj, pathcost, heuristic):
        self.vertex = vertex
        self.adj = adj
        self.pathcost = pathcost
        self.heuristic = heuristic


class Node:
    def __init__(self, node, parent, cost, tcost):
        self.node = node
        self.parent = parent
        self.cost = cost
        self.tcost = tcost


graph = []
path = []
ini = Node(0, 0, 0, 0)
p_queue = [ini]
des = 4
graph.append(node({0, 'S'}, [1, 2], [1, 4], 7))
graph.append(node({1: 'A'}, [2, 3, 4], [2, 5, 12], 6))
graph.append(node({2: 'B'}, [3], [2], 2))
graph.append(node({3: 'C'}, [4], [3], 1))
graph.append(node({4: 'D'}, [], [], 0))

while (len(p_queue) > 0):
    current = p_queue[0]
    if (current.node == des):
        break
    p_queue.pop(0)
    j = 0
    for i in graph[current.node].adj:
        nod = i
        gn = current.cost + graph[current.node].pathcost[j]
        hn = graph[current.node].heuristic
        gn_hn = gn + hn
        print(nod, gn, hn, gn_hn)
        p_queue.append(Node(nod, current, gn, gn_hn))
        p_queue.sort(key=lambda a: a.tcost)
        j = j + 1

Cost = current.cost
while (current.parent != 0):
    path.insert(0, graph[current.node].vertex)
    current = current.parent

path.insert(0, {0, 'S'})
print(f'Path: {path}')
print(f'Cost: {Cost}')
