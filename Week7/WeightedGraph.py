class Stack:
     def __init__(self):
         self.items = []

     def empty(self):
          if len(self.items) == 0:
               return True
          else:
               return False
               
     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def __str__(self):
          return "Stack: "+str(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
          if len(self.items) == 0:
               return True
          else:
               return False
          
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Graph(object):

     def __init__(self):
          self.graph = {}

     def addNode(self , node):
          self.graph[node]=[]
        
     def addEdge(self , nodeA , nodeB):
          self.graph[nodeA].append(nodeB)
          self.graph[nodeB].append(nodeA)

     def add(self , nodes , connections):
          for Node in nodes:
               self.addNode(Node)
    
          for First , Second in connections:
               self.addEdge(First , Second)
               
     def DepthFS(self, StartNode):
          S = Stack()
          Visited = []
          S.push(StartNode)
          while not S.empty():
               u = S.pop()
               if u not in Visited:
                    Visited.append(u)
                    for e in self.graph[u]:
                         S.push(e)
          return Visited

     def BreadthFS(self, StartNode):
          Q = Queue()
          Visited = []
          Q.enqueue(StartNode)
          while not Q.empty():
               u = Q.dequeue()
               if u not in Visited:
                    Visited.append(u)
                    for e in self.graph[u]:
                         Q.enqueue(e)
          return Visited
                    
            

nodes = ['A','B','C','D','E','F','G','H','S']
connections = [('A', 'B'),('A', 'S'),('S', 'G'),('G', 'F'),('D', 'C'),('F', 'C'),('S','C'),('E','C'),('G','H'),('H','E')]
g = Graph()
g.add(nodes,connections)
print(g.graph)
print("Depth First Search Result: " + str(g.DepthFS('A')))
print("Breadth First Search Result: " + str(g.BreadthFS('A')))
