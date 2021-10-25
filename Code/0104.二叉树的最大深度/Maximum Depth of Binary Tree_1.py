# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    采用递归的方法，判断当前节点左、右子树的深度，最大的深度即为该节点的深度，
    一层一层的递归上去，就可以找到根节点的最大深度
    """
    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)

    def getDepth(self, node):
        if node is None:
            return 0
        left_depth = self.getDepth(node.left)
        right_depth = self.getDepth(node.right)
        depth = 1 + max(left_depth, right_depth)
        return depth
