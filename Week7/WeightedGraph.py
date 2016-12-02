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
               self.addNode(Node)#Adds nodes to graph, from provided list called nodes
    
          for First , Second in connections:
               self.addEdge(First , Second) #Add edges to graph, from provided list of tuples including edges and weights called connections
               
     def DepthFS(self, StartNode):
          S = Stack() #initialises stack
          Visited = [] #list initialised for nodes that have been visited
          S.push(StartNode) # StartNode added to Stack S
          while not S.empty(): #while s isnt empty
               u = S.pop() # U becomes the last added element to Stack S
               if u not in Visited:
                    Visited.append(u) # Add u to visited if hasnt been visited before
                    for e in self.graph[u]: 
                         S.push(e) # Adds, one by one, to stack the nodes connected to U
          return Visited

     def BreadthFS(self, StartNode):
          Q = Queue() #Initialises Queue
          Visited = [] #list initialised for nodes that have been visited
          Q.enqueue(StartNode) #Adds StartNode to Queue Q
          while not Q.empty(): # While Q isnt empty
               u = Q.dequeue() # U becomes the first added element in Queue Q
               if u not in Visited:
                    Visited.append(u)# Add u to Visited if hasnt been visited before
                    for e in self.graph[u]:
                         Q.enqueue(e)# Adds, one by one, to queue the nodes connected to U
          return Visited
                    
            

nodes = ['A','B','C','D','E','F','G','H','S']
connections = [('A', 'B'),('A', 'S'),('S', 'G'),('G', 'F'),('D', 'C'),('F', 'C'),('S','C'),('E','C'),('G','H'),('H','E')]
g = Graph()
g.add(nodes,connections)
print(g.graph)
print("Depth First Search Result: " + str(g.DepthFS('A')))
print("Breadth First Search Result: " + str(g.BreadthFS('A')))
