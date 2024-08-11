'''class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        value = self.top.value
        self.top = self.top.next
        print(f"Popped {value} from stack")
        return value

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        print(f"Top of stack is {self.top.value}")
        return self.top.value


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.peek()  
stack.pop()  
stack.pop()   
'''

class Stack :
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkStack :
    def __init__(self):
        self.top = None
    
    def push(self,value):
        newn = Stack(value)
        if self.top is None :
            self.top = newn
            print("added")
            return
       
        newn.next = self.top
        self.top = newn
        print("added")

    def pop(self):
        if self.top is None:
            print("the tscak is empty ")
            return
        val = self.top.value
        self.top = self.top.next
        print("the ",val," is removed")

    def topv(self):
        if self.top is None:
            print("The  stake is meoty ")
            return
        print("the top value is" ,self.top.value)
        return self.top.value
    
    def isempty(self):
        if self.top is None:
            return True
        else :
            return False
    

news = LinkStack()
news.push("kerala")
news.push("AP")
news.push("TN")
news.push("US")
news.topv()
news.pop()
news.topv()
news.pop() 
news.topv()  

        