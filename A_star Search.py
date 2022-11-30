node = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
adj = [[1, 2], [2, 3, 4], [3], [4], []]
cost = [[1, 4], [2, 5, 12], [2], [3], []]
h_of_n = [7, 6, 2, 1, 0]


class Node:
    def __init__(self, node, parent, actual_cost, total_cost):
        self.node = node
        self.parent = parent
        self.actual_cost = actual_cost
        self.total_cost = total_cost


initial = Node(0, 0, 0, 0)
destination_node = 4
p_queue = [initial]
while (len(p_queue) != 0):
    current_node = p_queue[0]
    print("Extracted node:", current_node.node, 'Cost:', current_node.actual_cost)
    if (current_node.node == destination_node):
        print("Destination Found.")
        break
    p_queue.pop(0)
    for i in range(len(adj[current_node.node])):
        next_node = adj[current_node.node][i]
        gn = current_node.actual_cost + cost[current_node.node][i]
        hn = h_of_n[next_node]
        gn_hn = gn + hn
        print("Next adj node:", next_node, 'Parent cost:', current_node.actual_cost, 'gn:', gn, 'hn:', hn, 'gn_hn',
              gn_hn)
        p_queue.append(Node(next_node, current_node, gn, gn_hn))
        p_queue.sort(key=lambda x: x.total_cost)
    print("New P_Queue:")
    for q in p_queue:
        print(q.node, q.parent.node, q.actual_cost, q.total_cost)

Cost=current_node.actual_cost
path = [node[0]]
while (current_node.parent != 0):
    path.insert(1,node[current_node.node])
    current_node = current_node.parent


print('Source to Destination Cost:',Cost,'& Path:',path)
