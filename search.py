class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
       
    def search(self, val):
        curr=self.head
        while curr!=None:
            if val==curr.data:
                print("Value exists")
                return
            else: print("Value exists")
            curr=curr.next
