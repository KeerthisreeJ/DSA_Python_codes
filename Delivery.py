class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
'''
class Stacklink:
    def __init__(self) :
        self.top = None

    def push(self,value):
        drone = node(value)
        if self.top is None:
            self.top = drone
            return 
        drone.next = self.top
        self.top = drone

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
'''    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def adddrones(self,value):
        newn = node(value)
        if self.head is None:
            self.head = newn
            self.tail = newn
            return
        
        iter = self.head
        if self.head.value <= value:
                newn.next = self.head
                self.head.prev = newn
                self.head = newn
                return

        if self.tail.value >= value :
            self.tail.next = newn
            newn.prev = self.tail
            self.tail = newn
            return
        while iter :
            if (iter.value < value):
                newn.next = iter
                newn.prev = iter.prev
                iter.prev.next = newn
                iter.prev = newn
                return
            iter = iter.next

    def Loaddrone(self,value):
        if self.head is None:
            return 
        iter = self.head
        check = self.head.value
        while iter:
            if iter.value > check :
                check = iter.value
            
            iter = iter.next

    def display (self):
        iter = self.head
        while iter:
            print(iter.value, end=" -> ")
            iter = iter.next
        print("None")

    
drone = LinkedList()
drone.adddrones(23) 
drone.adddrones(3) 
drone.adddrones(253) 
drone.adddrones(213) 
drone.adddrones(2) 
drone.adddrones(253)
drone.adddrones(3)  
drone.display()       
        
        