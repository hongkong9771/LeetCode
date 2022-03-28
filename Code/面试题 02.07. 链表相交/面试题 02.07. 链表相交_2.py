# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        假设headA链表的长度为a，headB链表的长度为b，相交链表的长度为c
        指针A和指针B分别同时从headA、headB两个链表出发，当指针A走完headA链表后，再走headB链表；
        同样地，当指针B走完指针headB链表后，再走headA链表。一共有以下两种情况：
        1.若两个链表不相交。则会在同时走到两个链表的末端时相遇，即curA=None，curB=None。
        此时，走的长度为a+b
        2.若两个链表相交，则会在同时走到两个链表相交处相遇，即curA=curB，此时headA走的长度为a+b-c，
        headB走的长度为b+a-c
        """
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA