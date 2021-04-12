from node import Node
from singlylinkedlist import LinkedList


llist = LinkedList()
llist.head = Node(30)
llist.push(30)
llist.push(25)
llist.push(20)
llist.push(20)
llist.push(15)
llist.printList()

def removeDuplicates(llist):
    temp = llist.head
    if temp is None:
        return
    while temp is not None:
        if temp.data == temp.next.data:
            prev = temp
            temp = temp.next
            prev.next = temp.next
        temp = temp.next
        
removeDuplicates(llist)
print("removed")
llist.printList()

# O(n) time