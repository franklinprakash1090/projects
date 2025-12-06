class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return "Underflow! Stack is empty."
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    # Recursive function to display stack elements
    def display_recursive(self):
        if self.is_empty():
            return
        value = self.pop()
        print(value, end=" ")
        self.display_recursive()
        self.push(value)  # Restore original stack


# Main Program
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Stack elements (Recursive Display):")
s.display_recursive()

print("\nTop element:", s.peek())
print("Popped element:", s.pop())

print("Stack elements after pop:")
s.display_recursive()
