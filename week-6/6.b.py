# Queue Implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "enqueued into queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow.")
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(data, "dequeued from queue.")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("Queue elements:")
            while temp is not None:
                print(temp.data)
                temp = temp.next

# Main Program
q = Queue()
while True:
    print("\n======= QUEUE USING LINKED LIST =======")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    print("=========================================")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        q.enqueue(data)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
