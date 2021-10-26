# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 采用递归方法
        if root is None:
            return 0
        left_count = self.countNodes(root.left)
        rihgt_count = self.countNodes(root.right)
        count = 1 + left_count + rihgt_count    # 树的总的节点个数为当前根节点加上左右子树的节点个数总和
        return count