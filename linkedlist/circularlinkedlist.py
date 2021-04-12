from node import Node

class CircularLinkedList():
    def __init__(self):
        self.head = None

    # insert a new node end of the circular linked list
    def append(self, data):
        new_node = Node(data)
        temp = self.head
        while temp is not self.tail:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

        
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
            if temp is  self.head:
                break

"""cclist = CircularLinkedList()
cclist.head = Node(1)
second = Node(2)
cclist.head.next = second
cclist.tail = Node(3)
second.next = cclist.tail
cclist.tail.next = cclist.head
cclist.append(34)
print(cclist.head.next.next.next.next.data)
cclist.printList()"""