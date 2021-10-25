# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        采用迭代的方式解决，此题与LC第101题类似，一个是判断树是否对称，只需先分别比较左右子节点的外侧，再比较内测即可，
        而此题则是直接比较对应位置处的节点
        """
        # 迭代
        queue = []
        
        queue.append(p)
        queue.append(q)
        while len(queue) > 0:
            node_p = queue.pop(0)
            node_q = queue.pop(0)
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:      # 当两个节点只有一个为空，或者两个节点均不为空但值不相等时
                return False
            queue.append(node_p.left)
            queue.append(node_q.left)
            queue.append(node_p.right)
            queue.append(node_q.right)
        return True   