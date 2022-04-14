# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        使用最小堆存储每一个数，然后出堆，构建链表
        """
        if not lists:
            return None
        import heapq        # 引入堆
        min_heap = []       # 最小堆
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                heapq.heappush(min_heap, cur.val)
                cur = cur.next
        dummy_node = ListNode(0)    # 构建虚拟头节点
        tmp = dummy_node
        while min_heap:
            min_value = heapq.heappop(min_heap)
            node = ListNode(min_value)
            tmp.next = node
            tmp = tmp.next
        return dummy_node.next
