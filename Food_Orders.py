class node:
    def __init__(self,value) :
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.station = ["soup","sandwich","dessert"]
        self.orders = []

    def Order(self,cat,statno):
        food = node({'key':cat,'value':statno})
        m = 0
        for i in self.station:
            if(i == cat):
                m +=1
        if statno > m :
            return

        if self.head is  None:
            self.head = food
            self.tail = food
            self.orders.append(cat)
            #self.Orders.append({'key':cat,'value':statno})
            print(f"the order {cat} is added")
            return
        self.tail.next = food
        self.tail = food
        self.orders.append(cat)
        print(f"the order {cat} is added")
    
    #combine The order number is to be generated by combining the station number and the order number. For example, order ‘Soup order 3.8’ is order 8 and is delivered from soup station #3.
    def delivery(self,cat,statno):
        m = 0
        for i in self.station:
            if(i == cat):
                m +=1
        if statno > m :
            return
        
        if self.head is None:
            print("nothing is ordered")
            return
        iter = self.head
        j =0
        while iter.next:
            if (iter.value['key'] == cat):
                j+=1
            if(iter.value['key'] == cat and iter.value['value'] == statno):
                print(f"{cat} order {statno}.{j} delivered ")
                break
            iter = iter.next
        

    def add_stat(self,cat):
        self.station += [cat]
        print(cat ,"is added ")

    def most_common(self):
        s =0
        d =0
        sa = 0
        iter = self.head
        while iter.next:
            if ((iter.value['key']) == "soup"):
                s+=1
            elif ((iter.value['key']) == "sandwich"):
                sa+=1
            else :
                d+=1

        if (s>d and s>sa):
            print("Soup")
        elif (d>s and d>sa):
            print("dessert")
        else :
            print("Sandwich")
        
    def NoStation(self):
        print(len(self.station))

od = Linkedlist()
od.Order("soup" ,1)
od.Order("soup" ,1)
od.Order("Sandwich" ,1)
od.Order("dessert" ,1)
od.Order("soup" ,1)
od.add_stat("soup")
od.Order("soup" ,2)
od.delivery("soup",2)
od.delivery("soup",1)
od.delivery("dessert",1)
od.most_common()
od.NoStation()


                



        

        
        