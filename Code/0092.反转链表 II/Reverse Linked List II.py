# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
        找到反转链表区域的四个定位节点，分别为反转链表左边界的左边一个节点pre，左边界节点left_node，
        反转链表右边界的右边一个节点tail，右边界节点right_node
        本体定义了一个虚拟节点，以免出现空链表等情况
        '''
        def reverse_link_list(head: ListNode):
            """
            定义一个反转链表的函数
            """
            pre = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
        
        # 定义一个虚拟头节点
        virtual_node = ListNode(0)
        virtual_node.next = head
        pre = virtual_node

        # 定位四个节点
        for _ in range(left-1):
            pre = pre.next                  # 反转链表的左边界的左边一个节点
        
        left_node = pre.next                # 反转链表的左边界

        right_node = pre
        for _ in range(right-left+1):
            right_node = right_node.next    # 反转链表的右边界
        
        tail = right_node.next              # 反转链表的右边界的右边一个节点

        # 断掉链表的连接
        pre.next = None
        right_node.next = None

        # 反转链表
        reverse_link_list(left_node)

        # 将反转后的链表与前后的节点连接起来
        pre.next = right_node
        left_node.next = tail
        return virtual_node.next







                
