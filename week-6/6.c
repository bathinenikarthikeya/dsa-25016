class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        print(data, "enqueued into queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow.")
        elif self.front == self.rear:
            data = self.front.data
            self.front = None
            self.rear = None
            print(data, "dequeued from queue.")
        else:
            data = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
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
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.front:
                    break

# Main Program
cq = CircularQueue()
while True:
    print("\n======= CIRCULAR QUEUE USING LINKED LIST =======")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    print("==================================================")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        cq.enqueue(data)
    elif choice == 2:
        cq.dequeue()
    elif choice == 3:
        cq.peek()
    elif choice == 4:
        cq.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
