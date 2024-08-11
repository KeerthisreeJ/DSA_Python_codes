class CircularQueue :
    def __init__(self,n) :
        self.queue = [None]*n
        self.front = 0
        self.rear = -1
        self.n = n 

    def size(self):
        return (self.rear - self.front +self.n)%self.n
    
    def is_empty(self):
        return self.size() == 0
    
    def is_full(self):
        return self.size == self.n -1

    def enqueue(self,value):
        if self.is_full():
            print("the queue is full")
            return
        else :
            self.queue[self.rear]=value
            self.rear = (self.rear +1)%self.n

    def dequeue (self):
        if self.is_empty():
            print("the lsit is empty ")
            return
        else :
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front +1)%self.n

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[(self.rear - 1 + self.n) % self.n]









        