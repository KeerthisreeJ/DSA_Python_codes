class Queue :
    def __init__(self, n ):
       self.queue = [None]*n
       self.front = 0
       self.rear = -1
       self.n = n 

    def size(self):
        return self.rear - self.front +1 
    
    def is_empty(self):
        return self.size()==0
    
    def is_full(self):
        return self.size() == self.n
    
    def enqueue(self, value):
        if self.is_full():
            print("Tht Queue is full, if u want to add something dequeue and then enqueue")
            return
        else :
            self.rear +=1
            self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("The Queue is empty ")
            return None
        else :
            value = self.queue[self.front]
            self.front +=1
            return value
        
    def front(self):
        if self.is_empty():
            print("The Queue is empty ")
            return None
        else:
            return self.queue[self.front]
        
    def rear(self):
        if self.is_empty():
            print("The Queue is empty ")
            return None
        else :
            return self.queue[self.rear]
    
            

    

