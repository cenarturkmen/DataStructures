#using 2 stack, enqueue cost o(n)
#first in first out
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # o(n) time complexity
    def enQueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    #o(1) time complexity
    def deQueue(self):
        if len(self.s1) == 0:
            return print("error")

        popped = self.s1[-1]
        self.s1.pop()
        return popped


que = Queue()
que.enQueue(1)
que.enQueue(2)
que.enQueue(3)
que.enQueue(4)
print(que.s1)
que.deQueue()
print(que.s1)


