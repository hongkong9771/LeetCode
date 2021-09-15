# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_node = ListNode()
        c1, c2 = l1, l2
        cs = sum_node
        while c1 or c2:
            if c1:
                v1 = c1.val
            else:
                v1 = 0
            if c2:
                v2 = c2.val
            else:
                v2 = 0
            yu = (v1 + v2 + cs.val) % 10
            sh = (v1 + v2 + cs.val) // 10
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
            cs.val = yu
            
            if c1 or c2 or sh > 0:
                cs.next = ListNode(sh)
                cs = cs.next
        return sum_node