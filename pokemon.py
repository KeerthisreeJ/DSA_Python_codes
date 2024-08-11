class Pokemon:
    def __init__(self,name):
        self.name = name
        self.level = 2
        self.nature = "electric"

class node:
    def __init__(self,value) :
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self) :
        self.head = None
        self.u = []
        self.r = []
        
    def create_poke(self,name):
        newn = node(Pokemon(name))
        if self.head is None:
            self.head = newn
            print(name," is created ")
            return
        iter = self.head
        while iter.next:
            iter = iter.next
        
        iter.next = newn
       
        print(name," is created ")

    def feeding(self,value):
        if self.head is None:
            print("No pokemon is created")
            return
        iter = self.head
        check = True
        while(iter.next):
            
            if iter.value.name == value:
                print("Performed feeding activity for",value)
                self.u.append({'key': value,'value' :"feeding"})
                break
            else :
                check = False
            iter = iter.next
        if(check is False):
            print("there is no pokemon with the name",value)
            
    def training(self,value):
        if self.head is None:
            print("No pokemon is created")
            return
        iter = self.head
        check = True
        while(iter.next):
            
            if iter.value.name == value:
                self.u.append({'key': value,'value' :"training"})
                print("Performed training activity for",value)
                break
            else :
                check = False
            iter = iter.next
            
        if(check is False):
            print("there is no pokemon with the name",value)

    def battling(self,value):
        if self.head is None:
            print("No pokemon is created")
            return
        iter = self.head
        check = True
        while(iter.next):
           
            if iter.value.name == value:
                self.u.append({'key': value,'value' :"battling"})
                print("Performed battling activity for",value)
                break
            else :
                check = False
            
            iter = iter.next
        
        if(check is False):
            print("there is no pokemon with the name",value)

    def Undo(self,name):
        if len(self.u ) == 0:
            print("Cannot undo. No previous activity available for",name)
            return
        for i in reversed(range(len(self.u))):
            j = self.u[i]
            if (j['key'] == name):
                self.r.append(j)
                self.u.pop(i)
                print(f"Undo last activity for {name} : {j['value']}")
                break
        print("there is no pokemon with that name ")

    def redo(self,name):
        if len(self.r ) == 0:
            print("Cannot redo. No undone activity available for",name)
            return
        for i in reversed(range(len(self.r))):
            j = self.r[i]

            if (j['key'] == name):
                self.u.append(j)
                self.r.pop(i)
                print(f"Redo last activity for {name} : {j['value']}")
                return
            
        print("there is no pokemon with that name ")

    def favorite(self,name):
        train = 0
        feed = 0
        battle = 0
        for i in range(len(self.u)):
            j = self.u[i]
            if (j['key'] ==name):
                if(j['value'] == "feeding"):
                    feed+=1
                elif(j['value'] == "training"):
                    train+=1
                else:
                    battle+=1

        if (train >= feed and train >=battle)  :
            print(name ,"'s favourite activity : training" )  
            
        elif (feed >= train and feed >=battle)  :
            print(name ,"'s favourite activity : feeding" )
        else :
            print(name ,"'s favourite activity : battling" )
        
            
            
        

        
poke = Linkedlist()
poke.create_poke("Pikachu")
poke.create_poke("charmander")
poke.feeding("Pikachu")
poke.training("Pikachu")
poke.battling("Pikachu")
poke.training("Pikachu")
poke.battling("Pikachu")
poke.training("Pikachu")
poke.battling("Pikachu")
poke.training("Pikachu")
poke.favorite("Pikachu")




        
