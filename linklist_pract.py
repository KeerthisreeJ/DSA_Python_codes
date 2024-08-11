class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_Beginning(self,value):
        newnode = Node(value) # since its a new node, we are creating a instance of node
        newnode.next = self.head # the new node's next is the head
        self.head = newnode # since its going to bethe first element we are making the current element as the head
        
    def insert_at_end(self,value):
        new = Node(value)

        if self.head is None:
            self.head = new
            return
        
        now = self.head
        while(now.next) is not None:# its iterating to the end of the list 
            now = now.next#the now element is the last element, the address of the next element

        now.next = new # our required element is being added 

        
        '''
        Initialization:
        a linked list with nodes [1 -> 2 -> 3 -> 4] and we want to insert the value 5 after the 2nd node (2)
        new_node = Node(5)
        current = self.head (points to 1)
        Traverse to the k-th Node:

        For k=2, the loop runs once (k-1), moving current to 2.
        Insert the New Node:

        new_node.next = current.next (new node's next points to 3)
        current.next = new_node (2's next now points to the new node 5)
        The list now looks like: [1 -> 2 -> 5 -> 3 -> 4].'''
    def insert_at_kth(self,value,k):
        newn = Node(value)
        now = self.head
        if(self.head is None):
            self.head = newn
            return
        
        for _ in range (k-1):
            now = now.next #For k=2, the loop runs once (k-1), moving current to 2
           
           
        newn.next = now.next #The first line sets the next pointer of the new node to point to the node that currently follows the k-th node (current.next). This ensures the new node is linked to the rest of the list.
        now.next = newn#The second line updates the next pointer of the k-th node (current) to point to the new node. This inserts the new node into the list immediately after the k-th node.


    def delete_at_start(self):
        if (self.head is None):
            print("its empty")
            return
        x = self.head.value
        self.head = self.head.next
        return x
    

    def delete_at_mid(self,value):
        if(self.head is None):
            print("its emmpty")
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return value
        
        iter = self.head
        while iter.next:
            if iter.next.value == value:
                iter.next = iter.next.next
                return
            iter = iter.next 

    def delete_at_end(self):
        if(self.head is None):
            print("its emmpty")
            return
        iter = self.head
        while iter.next.next is not None:
            iter = iter.next
        iter.next = None

    def display(self):
        iter = self.head
        while iter:
            print(iter.value, end=" -> ")
            iter = iter.next
        print("None")

link = LinkedList()
link.insert_in_Beginning(3)
link.display()
link.insert_in_Beginning(1)
link.display()
link.insert_in_Beginning(0)
link.display()

link.insert_at_end(4)
link.display()
link.insert_at_kth(2,2)
link.display()


link.display()

link.delete_at_start()
link.display()
link.delete_at_mid(3)
link.display()
link.delete_at_end()

link.display()







    
    






                


