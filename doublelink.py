class node:
    def __init__(self, value) :
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None

    def insert_in_beginning(self,value):
        newn = node(value)
        if (self.head is None):
            self.head = newn
            print("added at the beginning")
            return
        newn.next = self.head
        self.head.prev = newn
        print("added at the beginning")
        
    def insert_in_end(self,value):
        newn = node(value)
        if(self.head is None):
            self.head = newn
            self.tail = newn
            print("added at the Ending")
            return
        self.tail.next = newn
        newn.prev = self.tail
        self.tail = newn
        print("added at the Ending")

    def insert_at_kth(self,value,k):
        newn = node(value)
        if(self.head is None):
            self.head = newn
            print("added at the Beginning ")
            return
        iter = self.head
        for _ in range(k-1):
            iter = iter.next
        
        
        newn.next = iter.next
        iter.next = newn
        newn.prev = iter
        iter.next.prev = newn
        print("added at the kth elemt ")

        


        

        