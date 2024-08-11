class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class Linkedlist :
    def __init__(self) :
        self.head = None
        self.tail = None

    def adduser(self, Id):
        newu = Node(Id)
        if (self.checkunique(Id) == False):
            return
        if (self.head is None):
            self.head = newu
            self.tail = newu 
            print(Id,"Added")
            return
        self.tail.next = newu
        newu.prev = self.tail
        self.tail = newu
        self.sortuser()
        print(Id,"Added")

    def deletion(self,id):
        if (self.head is None):
            print("No user to dlete")
            return
        
        iter = self.head
        while iter.next:
            if iter.value == id:
                if iter.prev and iter.next :
                    iter.prev.next = iter.next
                    iter.next.prev = iter.prev
                elif not iter.prev:
                    iter.next.prev = None
                    self.head = iter.next
                elif not iter.next:
                    iter.prev.next = None
                    self.tail = iter.prev
                return id
            iter = iter.next
        return None

        
    def sortuser(self):
        if self.head is None:
            return
        
        iter = self.head.next
        while iter:
            key = iter.value
            pre = iter.prev
            while pre and pre.value > key:
                pre.next.value = pre.value
                pre = pre.prev
            
            if pre:
                pre.next.value = key
            else :
                self.head.value = key
            
            iter = iter.next

    def searchmet(self,id):
        if self.head is None:
            return
        iter = self.head
        while iter.next:
            if iter.value == id:
                return id
            iter = iter.next
        return None
    
    def display (self):
        
        iter = self.head
        while iter:
            print(iter.value,end=" -> ")
            iter = iter.next
        print("End")

    def checkunique(self,id):
        iter = self.head
        while iter:
            if id == iter.value:
                print("the user name is already there")
                return False
            iter=iter.next
        return True
            
new = Linkedlist()
new.adduser("XOXOJan")
new.adduser("HArini_10")
new.adduser("Has...")
new.display()
#new.adduser("HArini_10")
new.deletion("Has...")
new.display()
new.adduser("a")
new.adduser("b")
new.display()

            
        