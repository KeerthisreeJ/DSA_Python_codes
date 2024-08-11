"""class participant:
    def __init__(self):

        self.next = None
        

class event :
    def __init__(self,value):
        self.value = value
        self.next = None
    
class registration:
    def __init__(self):
        self.head = None
        self.tail = None

    def createevent(self,value):
        eve = event(value)
        if(self.head is None):
            self.head = eve
            self.tail = eve
            print(f"Event {value} added")
            return
        self.tail = eve
        print(f"Event {value} added")

    def registera

        

        
        """

class node :
    def __init__(self,value,resources,buildings ) :
        self.value = value
        self.resources = resources
        self.buildings = buildings
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def create_city(self,value ,resources,buildings ):
        newc = node(value,resources,buildings,)
        if (self.head is None):
            self.head = newc
            print("your city has been ceated with the name" ,value )
            return
        iter = self.head
        while iter.next :
            iter = iter.next

        iter.next = newc
        print("your city has been ceated with the name" ,value )

        