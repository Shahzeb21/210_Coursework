class Node(object):

    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
        
 
class List(object):

    def __init__(self):
        self.head=None
        self.tail=None


    def insert(self,n,x):
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    # Adding DeleteNode Method here
    def delete (self, N): # N being the node you want to delete
        if N.prev != None:
            N.prev.next = N.next #if the node to be deleted is not the first, then the node after takes position of N
        else:
            self.head = N.next #if the first node is to be deleted, then the node after becomes the first node
        if N.next != None:
            N.next.prev = N.prev #if the node N is not the last node then next node takes position of N.
        else:
            self.tail = N.prev #if N is the last node then the node before it becomes last node.            

    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print (values)
        
         
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))

    l.display()
    l.delete(l.head.next.next)
    l.display()
