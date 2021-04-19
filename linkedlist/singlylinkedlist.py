from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # insert a new node at the front of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # insert a new node after the given prev_node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("ERROR")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # insert a new node end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next is not None :
            last = last.next

        last.next = new_node

    #  delete the first occurence of key in linked list
    #**
    def deleteNode(self, key):

        temp = self.head
 
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
 
        prev.next = temp.next
        temp = None

    # Given a singly linked list and a position, delete a linked list node at the given position.
    def deleteNodePosition(self,position):
        temp = self.head

        for i in range(position-1):
            prev = temp
            temp = temp.next

        prev.next = temp.next

    # In Java and Python, automatic garbage collection happens, so deleting a linked list is easy. Just need to change head to null.
    def deleteLinkedList(self):
        self.head = Null

    # count the number of nodes in a given singly linked list.
    def length(self):
        temp = self.head
        c = 0
        while temp is not None:
            temp = temp.next
            c = c + 1
        return c  

    def lengthRecursive(self,node):
        if not Node:
            return 0
        else:
            return 1 + self.lengthRecursive(node.next)
    
    def lengthRec(self):
        return self.lengthRecursive(self.head)

    #search an element in a linked list + recursive
    def search(self, x):
        temp = self.head
        while temp is not None:
            if x == temp.data:
                return True
            temp = temp.next    
        return False
    
    #Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position. 
    def getNth(self, position):
        temp = self.head
        for i in range(position):
            temp = temp.next
        return temp.data
        
    # get reverse of linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def reverseRecursive(self,head):
        if head is None or head.next is None:
            return head
        
        p = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return p


    # utility function 
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next






"""llist = LinkedList()
print("length: ",llist.length())
llist.head = Node(1)
second = Node(2)
third  = Node(3)
llist.head.next = second
second.next = third

llist.push(33)
llist.insertAfter(llist.head.next.next, 58)
llist.append(31)
llist.deleteNode(33)
llist.deleteNodePosition(2)
print(llist.search(355))
print(llist.getNth(3))
print("length: ",llist.length())
llist.printList()
llist.reverse()
llist.printList()
llist.reverseRecursive(llist.head)
llist.printList()
"""



