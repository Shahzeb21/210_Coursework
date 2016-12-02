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
        
     def addEdge(self , nodeA , nodeB, weight):
          self.graph[nodeA].append([nodeB,weight])
          self.graph[nodeB].append([nodeA,weight])

     def add(self , nodes , connections):
          
          for Node in nodes:
               self.addNode(Node)
    
          for First , Second , Weight in connections:
               self.addEdge(First , Second , Weight)
          

     def Dijkstra(self, source, destination):
          v = source
          tw={} # New Dictionary to store the connections and their new weights for initialise
          for n in self.graph:
                    tw[n] = 999 # Stores weight to 999 for all nodes except the source
          tw[v] = 0 # Value for key "v" which is the source is 0
          print(tw)
          Visited = [] # List initialised for visited nodes
          while v != destination:
               for Adj in g.graph[v]: # for nodes connected to the source
                    tw[Adj[0]]=tw[v]+Adj[1] # Calculates weight.
               v=Adj[0]
               for g4 in g.graph[v]:
                    tw[g4[0]]=tw[v]+g4[1]
               break
          print(tw)
          #I didnt go through with the whole Dijikstra's Algorithm, this si the partial solution that only calculates
          # the tentative weight from the source all the other nodes.
               
               
          
                


                   
            

nodes = ['A','B','C','D','E','F','G','H','S']
connections = [('A', 'B' , 2),('A', 'S' , 5),('S', 'G' , 3),('G', 'F', 4),('D', 'C' , 1),('F', 'C' , 4),('S','C' , 3),('E','C' , 2),('G','H' , 1),('H','E' , 2)]
g = Graph()
g.add(nodes,connections)
for g1 in g.graph:
     print(g1)
     print(str(g1)+":"+str(g.graph[g1]))
g.Dijkstra('A','F')
#print("Depth First Search Result: " + str(g.DepthFS('A')))
#print("Breadth First Search Result: " + str(g.BreadthFS('A')))


#https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm
