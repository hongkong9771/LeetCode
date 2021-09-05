# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        计算两个链表的长度，并将两个链表末端对齐。
        """
        curA = headA
        curB = headB
        lenA = 0
        lenB = 0
        while curA:
            curA = curA.next
            lenA += 1
        
        while curB:
            curB = curB.next
            lenB += 1
        
        curA, curB = headA, headB
        if lenA < lenB:
            lenA, lenB = lenB, lenA
            curA, curB = curB, curA
        diff = lenA - lenB

        for i in range(diff):
            curA = curA.next
        while curA and curB:
            if curA is curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
