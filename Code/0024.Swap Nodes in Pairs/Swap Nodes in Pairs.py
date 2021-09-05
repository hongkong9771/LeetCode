# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(0, head) # 构造虚拟头结点
        cur = dummy_node

        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = cur.next.next
            cur.next.next = temp
            cur = temp
            temp = temp.next
        return dummy_node.next