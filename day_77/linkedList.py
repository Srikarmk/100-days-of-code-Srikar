class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head==None:
            print("Linked List is Empty")
            return
        ptr=self.head
        statement=""
        while ptr:
            statement+=str(ptr.data)+"->"
            ptr=ptr.next
        print(statement)

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_start(5)        
    ll.insert_start(420)        
    ll.insert_start(69)
    ll.print()        

