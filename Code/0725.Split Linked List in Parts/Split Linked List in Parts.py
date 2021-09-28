# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
解题思路：
1.当链表的长度不够分成k份时，前面的cnt份均只有一个链表节点，将每一个链表节点的下一个节点保存之后，将cur.next赋为None
2.当链表的长度可以分成k份时，先计算每份应该存放几个链表节点，多余的链表节点往前存放，代码中用"yu"记录多余节点的个数。
"""
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        res = [None for _ in range(k)]
        cur = head
        cnt = 0     # 统计链表长度
        while cur:
            cnt += 1
            cur = cur.next
        cur = head
        yu = cnt % k
        sh = cnt // k
        if sh == 0:             
            for i in range(cnt):
                res[i] = cur
                temp = cur.next         # 此处三个赋值操作是为了断开链表节点
                cur.next = None
                cur = temp
        else:
            for i in range(k):
                res[i] = cur
                j = 0
                while j < sh - 1:
                    cur = cur.next
                    j += 1
                if yu != 0:
                    cur = cur.next
                    yu -= 1
                temp = cur.next         # 此处三个赋值操作是为了断开链表节点
                cur.next = None
                cur = temp
        return res