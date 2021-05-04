#https://leetcode.com/problems/reverse-linked-list
#recursive o(n)
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    if head is None or head.next is None:
        return head
        
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p

# o(n)
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head