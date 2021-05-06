# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 采用递归的方式求解
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left is not None and right is None:      # 当左节点不为空，但右节点为空时
            return False
        elif right is not None and left is None:    # 当右节点不为空，但左节点为空时
            return False
        elif left is None and right is None:        # 当左右节点均为空时
            return True
        elif left.val != right.val:                 # 当左右节点均不为空时，且值也不相等时
            return False
        else:                                       # 剩下的就是值相等的情况
            outside = self.compare(left.left, right.right)
            inside = self.compare(left.right, right.left)
            isSame = outside and inside
            return isSame