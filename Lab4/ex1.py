# Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack.items)
    print("Peek:", stack.peek())
    elem_removed = stack.pop()
    print("Pop:", elem_removed)
    print("Stack after pop:", stack.items)
    stack.push(100)
    print("New Stack after push:", stack.items)