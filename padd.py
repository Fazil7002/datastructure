class Stack:
    def __init__(self):  # Corrected constructor with double underscores
        self.stack = []
    
    def stack_operation(self, operation, value=None):
        if operation == 'push':  # Push operation
            if len(self.stack) >= 10:  # Stack overflow check (optional limit)
                print("Stack Overflow!")
            else:
                self.stack.append(value)
                print(f"Pushed {value} onto stack")
        elif operation == 'pop':  # Pop operation
            if len(self.stack) == 0:
                print("Stack Underflow!")
            else:
                popped_value = self.stack.pop()
                print(f"Popped {popped_value} from stack")
        else:
            print("Invalid operation. Use 'push' or 'pop'.")

# Example usage
stack = Stack()

stack.stack_operation('push', 10)  # Push 10
stack.stack_operation('push', 20)  # Push 20
stack.stack_operation('pop')       # Pop
stack.stack_operation('push', 30)  # Push 30
