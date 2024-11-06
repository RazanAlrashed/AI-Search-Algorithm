from queue import PriorityQueue
class Graph:
    def __init__(self):
        self.graph = {}
        self.heuristics = {}
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    def add_heuristic(self, node, heuristic):
        self.heuristics[node] = heuristic

def Greedy(graph, start, target):
    queue = PriorityQueue()
    visited = set()
    queue.put((0, start, [start]))  # (cost, node, path)
    
    while not queue.empty():
        cost, node, path = queue.get()  # get will remove and return from queue
        
        if node not in visited:
            visited.add(node)
            if node == target:
                return cost, path  
            
            for neighbor in graph.graph[node]:
                if neighbor not in visited:
                    total_cost = graph.heuristics.get(neighbor, 0)
                    queue.put((total_cost, neighbor, path + [neighbor]))
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('G')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'G')
g.add_edge('C', 'G')
g.add_edge('D', 'G')
g.add_heuristic('A', 10)
g.add_heuristic('B', 2)
g.add_heuristic('C', 5)
g.add_heuristic('D', 4)
g.add_heuristic('G', 0)
cost, path = Greedy(g, 'A', 'G')
print(f"PATH: {' -> '.join(path)}")
print(f"Cost from A to G: {cost}")
