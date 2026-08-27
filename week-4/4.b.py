class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    def insert_index(self, data, index):
        if index == 0:
            self.insert_begin(data)
            return
        if index < 0 or index > self.count():
            print("Invalid index")
            return
        new = Node(data)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new.next = temp.next
        temp.next = new
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
ll.insert_begin(10)
ll.insert_index(20, 1)
ll.insert_index(30, 2)
ll.insert_index(40, 3)
print("Original list:")
ll.display()
data = int(input("Enter data: "))
index = int(input("Enter index: "))
ll.insert_index(data, index)
print("After insertion:")
ll.display()
