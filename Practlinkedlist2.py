class node :
    def __init__(self,value):
        self.value = value
        self.next = None

class queuelink :
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        newn = node(value)
        if (self.head is None):
            self.head = newn
            self.tail = newn
            return
        self.tail.next = newn
        self.tail = newn
        print("added")

    def dequeue(self):
        if (self.head is None):
            print("Bhaiya, empty hai")
            return
        cur = self.head
        self.head = self.head.next
        return cur.value
    
    def front(self):
        return self.head.value
    
    def rear(self):
        return self.tail.value
    
    def size(self):
        num = 0
        iter = self.head
        while (iter.next is not None):
            iter= iter.next
            num +=1
        
        return (f"the Size of the queue infused linked list is {num}")
    
    def isempty(self):
        if self.head is None:
            return True
        else :
            return False
        
    def display(self):
        iter = self.head
        while iter:
            print(iter.value , end=" -> ")
            iter = iter.next
        print("None")
        
que = queuelink()
que.enqueue(1)
que.display()
que.enqueue(2)
que.display()
que.enqueue(3)
que.display()
que.dequeue()
que.display()
que.dequeue()
que.display()
que.dequeue()
que.display()
que.dequeue()
que.enqueue(1)
que.display()
que.front()
que.rear()
que.enqueue(2)
que.display()
que.enqueue(3)
que.display()
que.rear()

    


        
        
        