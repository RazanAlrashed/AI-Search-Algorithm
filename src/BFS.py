from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store graph.
        self.graph=defaultdict(list)
        # function for adding node and their nighbor
    def add(self,node,nighbor):
        self.graph[node].append(nighbor)
        # function to preform Bredth First Search.
    def BFS(self,start):
        visited=[]
        queue=[]
        visited.append(start)
        queue.append(start)
        
        while queue:
            m = queue.pop(0)
            print(m, end=" ")
            for neighbor in self.graph[m]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    
# create a graph instance from graph class.     
graph1=Graph()
graph1.add('1','2')    
graph1.add('2','3')    
graph1.add('2','4')    
graph1.add('2','5')    
graph1.add('3','6')    
# calling BFS function.
graph1.BFS('1')

#expected output:1 2 3 4 5 6 