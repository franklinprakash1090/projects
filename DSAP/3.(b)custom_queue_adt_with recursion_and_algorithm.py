class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Underflow! Queue is empty."
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    # Recursive function to display queue elements
    def display_recursive(self):
        if self.is_empty():
            return
        val = self.dequeue()
        print(val, end=" ")
        self.display_recursive()
        self.enqueue(val)  # Restore queue


# Main Program
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue elements (Recursive Display):")
q.display_recursive()

print("\nDequeued element:", q.dequeue())

print("Queue after dequeue:")
q.display_recursive()
