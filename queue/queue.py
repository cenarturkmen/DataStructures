class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.s = []
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.s.append(value)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.s.pop(0)
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[-1]


    def isEmpty(self) -> bool:
        if not self.s:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.s)==self.k:
            return True
        return False