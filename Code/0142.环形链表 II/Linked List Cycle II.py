# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:       # 防止head为空和出现空指针的next情况
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    slow = slow.next
                    fast = fast.next
                return fast
        return