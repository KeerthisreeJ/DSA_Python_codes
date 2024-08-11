class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_beginning(self, value):
        newn = node(value)
        if self.head is None:
            self.head = newn
            self.tail = newn
            print("added at the beginning")
            return
        newn.next = self.head
        self.head.prev = newn
        self.head = newn
        print("added at the beginning")
        
    def insert_in_end(self, value):
        newn = node(value)
        if self.head is None:
            self.head = newn
            self.tail = newn
            print("added at the Ending")
            return
        self.tail.next = newn
        newn.prev = self.tail
        self.tail = newn
        print("added at the Ending")

    def insert_at_kth(self, value, k):
        newn = node(value)
        if self.head is None:
            self.head = newn
            self.tail = newn
            print("added at the Beginning")
            return
        iter = self.head
        for _ in range(k-1):
            iter = iter.next
        
        newn.next = iter.next
        if iter.next:
            iter.next.prev = newn
        iter.next = newn
        newn.prev = iter
        if newn.next is None:
            self.tail = newn
        print("added at the kth element")

    def delete_in_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("deleted at the beginning")

    def delete_in_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print("deleted at the Ending")

    def delete_at_kth(self, k):
        if self.head is None:
            print("List is empty")
            return
        if k == 0:
            self.delete_in_beginning()
            return
        iter = self.head
        for _ in range(k-1):
            iter = iter.next
            if iter is None or iter.next is None:
                print("Position out of range")
                return
        to_delete = iter.next
        iter.next = to_delete.next
        if to_delete.next:
            to_delete.next.prev = iter
        if to_delete == self.tail:
            self.tail = iter
        print("deleted at the kth element")


newww = LinkedList()
newww.insert_in_beginning(6)
newww.insert_in_end(76)
