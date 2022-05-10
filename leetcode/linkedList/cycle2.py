# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def intersection(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return slow
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return None
        intersection = self.intersection(head)
        if intersection is None:
            return None
        start = head
        while start != intersection:
            start = start.next
            intersection = intersection.next
        return intersection
