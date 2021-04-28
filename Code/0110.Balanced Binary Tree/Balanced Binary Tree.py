# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        二叉树节点的高度定义为从该节点到叶子节点的最大节点数量
        二叉树节点的深度定义为从该节点到根节点的最大节点数量
        """
        if self.gethigh(root) == -1:
            return False
        else:
            return True
        
    def gethigh(self, node):
        if node is None:
            return 0
        left_high = self.gethigh(node.left)
        if left_high == -1:
            return -1
        right_high = self.gethigh(node.right)
        if right_high == -1:
            return -1
        if abs(left_high - right_high) <= 1:
            return 1 + max(left_high, right_high)
        else:
            return -1