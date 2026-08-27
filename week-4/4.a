class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
l=LinkedList()
n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input(f"Enter data for node {i + 1}: "))
    ll.insert_end(data)
    l.insert_begin(data)
print("Linked List:")
ll.display()
print("linkedlist1:")
l.display()
