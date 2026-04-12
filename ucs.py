class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, u, v, cost):
        self.add_node(u)
        self.add_node(v)
        self.adjacency_list[u].append((v, cost))


def ucs(graph, start, goal):
    frontier = [(Node(start), 0)]   # (node, path_cost)
    explored = set()

    while frontier:
        # choose node with smallest total path cost
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        print("Fringe:", [(n.state, c) for n, c in frontier])
        print("Visited:", explored)
        print("Expanding:", current_node.state, "Cost:", current_cost)
        print()

        if current_node.state == goal:
            explored.add(current_node.state)
            return current_node, current_cost

        explored.add(current_node.state)

        for child_state, step_cost in graph.adjacency_list[current_node.state]:
            new_cost = current_cost + step_cost

            # check if child is already in frontier
            found = False
            for i, (f_node, f_cost) in enumerate(frontier):
                if f_node.state == child_state:
                    found = True
                    if new_cost < f_cost:
                        frontier[i] = (Node(child_state, current_node), new_cost)
                    break

            if child_state not in explored and not found:
                frontier.append((Node(child_state, current_node), new_cost))

    return None, None


def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("Path:", " -> ".join(path))
graph = Graph()

n_nodes = int(input("Enter number of nodes: "))
for _ in range(n_nodes):
    graph.add_node(input())

n_edges = int(input("Enter number of edges: "))
for _ in range(n_edges):
    u, v, c = input().split()
    graph.add_edge(u, v, int(c))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result, cost = ucs(graph, start, goal)

if result:
    print("Goal Found! Path cost:", cost)
    print_solution(result)
else:
    print("Goal Not Found")
