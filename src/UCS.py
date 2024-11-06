from queue import PriorityQueue
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, value):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, value))
            self.graph[node2].append((node1, value))

def UCS(graph, start, target):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))  # (cost, node, path)
    
    while not queue.empty():
        cost, node, path = queue.get()  # get will remove and return from queue
        
        if node not in visited:
            visited.add(node)
            
            if node == target:
                return cost, path  
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + weight
                    queue.put((total_cost, neighbor, path + [neighbor]))
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'E', 2)
g.add_edge('B', 'D', 6)
g.add_edge('C', 'F', 5)
g.add_edge('F', 'G', 3)
g.add_edge('E', 'G', 8)
g.add_edge('D', 'G', 3)

cost, path = UCS(g.graph, 'A', 'G')
print(f"Path : {'->'.join(path)}")
print(f"Cost from A to G : {cost}")




   
          