from node import Node

#last in first out
class Stack():
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is not None: # or self.isEmpty == False
            temp = self.top
            self.top = temp.next
            popped = temp.data
            return popped

    def peek(self):
        if self.top is None:
            return None
        return self.top.data


"""stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("peek", stack.peek())
print("popped", stack.pop())
print("peek", stack.peek())"""
 
######################################
# Using array
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def push(stack, data):
    stack.append(data)

def pop(stack):
    if isEmpty(stack) == False:
        return stack.pop()

def peek(stack):
    if isEmpty(stack) == False:
        return(stack[-1])

"""stack = createStack()
push(stack, 34)
push(stack, 33)
push(stack, 32)
print("peek 1:", peek(stack))
print("pop 1:", pop(stack))
print("peek 2:", peek(stack))"""