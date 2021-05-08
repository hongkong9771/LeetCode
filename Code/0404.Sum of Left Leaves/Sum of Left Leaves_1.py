# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 递归采用后序遍历的思想
        if root is None:
            return 0
        leftValue = self.sumOfLeftLeaves(root.left)
        rightValue = self.sumOfLeftLeaves(root.right)

        value = 0
        if root.left and not root.left.left and not root.left.right:    # 若为左叶子节点，则赋值
            value = root.left.val
        res = value + leftValue + rightValue
        return res