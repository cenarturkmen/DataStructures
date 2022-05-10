# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        c = 0
        temp = head
        while temp is not None:
            temp = temp.next
            c = c + 1
        return c

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = self.getLength(headA)
        b = self.getLength(headB)
        listNodeA = headA
        listNodeB = headB
        if(a >= b):
            for i in range(a-b):
                listNodeA = listNodeA.next

            while listNodeA != listNodeB:
                listNodeA = listNodeA.next
                listNodeB = listNodeB.next
            if(listNodeA == listNodeB):
                return listNodeA
            return None
        if(b >= a):
            for i in range(b-a):
                listNodeB = listNodeB.next

            while listNodeA != listNodeB:
                listNodeA = listNodeA.next
                listNodeB = listNodeB.next
            if(listNodeA == listNodeB):
                return listNodeA
            return None
        # if(b==a):
        #     while listNodeA != listNodeB:
        #         listNodeA = listNodeA.next
        #         listNodeB = listNodeB.next
        #     if(listNodeA == listNodeB):
        #         return listNodeA
        #     return None
