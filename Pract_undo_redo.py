class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.history = []
        self.songs = []

    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.songs.append(song)
        print(f"The song '{song}' is added to the playlist")

    def play(self):
        if self.current is None:
            self.current = self.head

        if self.current:
            print(f"The song playing now is '{self.current.value}'")
            self.history.append(self.current)
        else:
            print("No songs in the playlist to play")

    def skip(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play()
        else:
            print("You are at the end of the playlist or there is no song to skip to")

    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play()
        else:
            print("You are at the beginning of the playlist or there is no song to go back to")

    def fav(self):
        song_play_count = {}
        for node in self.history:
            song = node.value
            if song in song_play_count:
                song_play_count[song] += 1
            else:
                song_play_count[song] = 1
        
        if song_play_count:
            fav_song = max(song_play_count, key=song_play_count.get)
            print(f"The favorite song is '{fav_song}' played {song_play_count[fav_song]} times")
        else:
            print("No songs have been played yet")
