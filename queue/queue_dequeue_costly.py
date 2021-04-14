
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # o(1) time complexity
    def enQueue(self,x):
        self.s1.append(x)

    # o(n) time complexity
    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return print("Error")

        elif len(self.s1) != 0 and len(self.s2) == 0:
            while self.s1 !=0:
                self.s2.append(self.s1[-1])
                self.s1.pop()
                return self.s2.pop()
                
        else:
            return self.s2.pop()





que = Queue()
que.enQueue(1)
que.enQueue(2)
que.enQueue(3)
que.enQueue(4)
print(que.s1)
que.deQueue()
print(que.s1)
que.enQueue(5)
que.enQueue(6)
que.enQueue(7)
que.enQueue(8)
print(que.s1)
que.deQueue()
print(que.s1)


    
