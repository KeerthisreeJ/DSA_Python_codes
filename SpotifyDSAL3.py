class Spotify:
    def Playlist(s):
        s.queue = []
        s.front=0
        s.rear=-1

    '''def increase(s):
        s.queue = '''
    def size(s):
        return len(s.queue)
    
    def add_song(s,value):
    
        s.queue += [value ]
        print("added")

    def remove_current(s):
        if (s.size() == 0):
            print("theres nothing to remove")
            return 
        value = s.queue[s.front]
        s.front +=1
        return value

    def display(s):
        for i in s.queue:
            if(i == None):
                i = " "
            print(i)



mus = Spotify()
mus.Playlist()
mus.add_song("Another love")
mus.add_song("An")
mus.add_song("love")
mus.add_song("Anoe")
mus.display()
print("_____")
mus.remove_current()
print("_____")
mus.display()


