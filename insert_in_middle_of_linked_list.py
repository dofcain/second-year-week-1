class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def insertAtMiddle(self, data):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        mid = count // 2
        curr = self.head
        for _ in range(mid - 1):
            curr = curr.next
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")
