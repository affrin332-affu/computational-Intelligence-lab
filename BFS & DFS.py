from collections import deque

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

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.adjacency_list[u].append(v)

    def delete_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
        for n in self.adjacency_list:
            if node in self.adjacency_list[n]:
                self.adjacency_list[n].remove(node)

    def delete_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)

    def display(self):
        print("\nGraph in Adjacency List:")
        for node in self.adjacency_list:
            if self.adjacency_list[node]:
                print(node, "->", self.adjacency_list[node])


def bfs(graph, start, goal):
    fringe = deque()
    visited = []

    start_node = Node(start)
    fringe.append(start_node)

    #print("\nFringe:")
    print("\nFringe:",[n.state for n in fringe])
    #print("Visited:")
    print("Visited:",visited)
    print()

    while fringe:
        current = fringe.popleft()
        visited.append(current.state)

        if current.state == goal:
            print("Fringe:",[])
            #print([])
            print("Visited:",visited)
            #print(visited)
            return current

        for neighbor in graph.adjacency_list.get(current.state, []):
            if neighbor not in visited and neighbor not in [n.state for n in fringe]:
                child = Node(neighbor, current)
                fringe.append(child)

        #print("Fringe:")
        print("Fringe:",[n.state for n in fringe])
        print("Visited:",visited)
        #print(visited)
        print()

    return None

def dfs(graph, start, goal):
    fringe = []
    visited = []

    start_node = Node(start)
    fringe.append(start_node)

    print("\nFringe:", [n.state for n in fringe])
    print("Visited:", visited)
    print()

    while fringe:
        current = fringe.pop()
        visited.append(current.state)

        if current.state == goal:
            print("Fringe:", [])
            print("Visited:", visited)
            return current

        neighbors = graph.adjacency_list.get(current.state, [])
        for neighbor in reversed(neighbors):
            if neighbor not in visited and neighbor not in [n.state for n in fringe]:
                child = Node(neighbor, current)
                fringe.append(child)

        print("Fringe:", [n.state for n in fringe])
        print("Visited:", visited)
        print()

    return None

def print_solution(goal_node):
    if goal_node is None:
        print("No path found.")
        return

    path = []
    current = goal_node

    while current:
        path.append(current.state)
        current = current.parent

    path.reverse()
    print("\nPath:", " -> ".join(path))
    print("Path Cost:", len(path) - 1)


graph = Graph()
result_node = None

n_nodes = int(input("Enter number of nodes: "))
print("Enter node names:")
for _ in range(n_nodes):
    node = input()
    graph.add_node(node)

n_e = int(input("Enter number of edges: "))
print("Enter edges in format: A B")
for _ in range(n_e):
    u, v = input().split()
    graph.add_edge(u, v)


while True:
    print("\n--- MENU ---")
    print("1. Add Node")
    print("2. Add Edge")
    print("3. Delete Node")
    print("4. Delete Edge")
    print("5. Display Graph")
    print("6. Perform BFS")
    print("7. Perform DFS")
    print("8. Print Path")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        node = input("Enter node: ")
        graph.add_node(node)

    elif choice == '2':
        u = input("Enter start node: ")
        v = input("Enter end node: ")
        graph.add_edge(u, v)

    elif choice == '3':
        node = input("Enter node to delete: ")
        graph.delete_node(node)

    elif choice == '4':
        u = input("Enter start node: ")
        v = input("Enter end node: ")
        graph.delete_edge(u, v)

    elif choice == '5':
        graph.display()

    elif choice == '6':
        start = input("Enter start state: ")
        goal = input("Enter goal state: ")
        result_node = bfs(graph, start, goal)
        if result_node:
            print("\nGoal Found!")
        else:
            print("\nGoal Not Found!")

    elif choice == '7':
        start = input("Enter start state: ")
        goal = input("Enter goal state: ")
        result_node = dfs(graph, start, goal)
        if result_node:
            print("\nGoal Found!")
        else:
            print("\nGoal Not Found!")


    elif choice == '8':
        print_solution(result_node)

    elif choice == '9':
        print("Exiting..")
        break

    else:
        print("Invalid choice. Try again.")
