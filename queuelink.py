class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {value} into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {value} from queue")
        return value

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        print(f"Front of queue is {self.front.value}")
        return self.front.value

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()    
queue.dequeue() 
queue.dequeue()
queue.dequeue() 