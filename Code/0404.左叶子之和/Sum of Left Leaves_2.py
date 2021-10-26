# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 采用迭代的思想解决
        if root is None:
            return 0
        queue = []
        queue.append(root)
        res = 0
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res