# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        # 当要删除的元素为第一个元素时
        while head and head.val == val:
            head = head.next
        else:
            cur = head
            pre = None              # 用于储存被删除节点的上一节点
            while cur is not None:  # 遍历到尾节点
                if cur.val != val:
                    pre = cur
                else:
                    pre.next = cur.next
                cur = cur.next
        return head