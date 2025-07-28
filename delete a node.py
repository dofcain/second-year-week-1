class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def deleteAtPosition(self, pos):
        if self.head is None:
            print("List is empty.")
            return

        # If deleting the head (position 0)
        if pos == 0:
            self.head = self.head.next
            return

        curr = self.head
        for i in range(pos - 1):
            if curr.next is None:
                print("Position out of bounds.")
                return
            curr = curr.next

        if curr.next is None:
            print("Position out of bounds.")
            return

        curr.next = curr.next.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")
