class AppleMusic:
    def playlist(Self,n):
        Self.queue = [None]*n
        Self.front = 0
        Self.rear = -1
        Self.n = n 

    def size(Self):
        return (Self.rear - Self.front + Self.n )%Self.n
    
    def add(Self, value):
        if (Self.size== Self.n ):
            Self.front = (Self.front +1)%Self.n
        
        Self.rear = (Self.rear +1)%Self.n 
        Self.queue[Self.rear] = value
        print("added")

    def remove(Self):
        if (Self.size == 0):
            print("List empty")
            return
        x = Self.front 
        Self.queue[Self.front] = None
        Self.front = Self.front+1

    def display(Self):
        for i in Self.queue:
            if(i == None):
                i = " "
            print(i, end=" ")
        

music = AppleMusic()
music.playlist(3)
music.add("coldplay")
music.add("cy")

music.add("play")
music.add("cold")

music.remove()
music.display()

