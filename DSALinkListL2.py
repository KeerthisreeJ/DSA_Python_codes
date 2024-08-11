class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_kth(self,value,k):
        newn = Node(value)
        if(self.head is None):
            self.head = newn
            return
        iter = self.head
        for _ in range(k-1):
           iter = iter.next
        iter.next = newn
        newn = iter.next.next
        return (f"Added the element of value {value} at the psoition {k}")
    
    def del_kth(self,value,k):
        if self.head is None:
            return None
        iter = self.head
        for _ in range(k-1):
            iter = iter.next
        iter.next = iter.next.next
        return True
    

link = LinkedList()

val = input("type:")
if (val == "insert"):
    x = input("text : ")
    o = int(input("position :"))
    link.insert_kth(x,o)
elif (val == "delete"):
    x = input("text : ")
    o = int(input("position :"))
    link.del_kth(x,o)
else :
    print("error wouldnt find")

        
        