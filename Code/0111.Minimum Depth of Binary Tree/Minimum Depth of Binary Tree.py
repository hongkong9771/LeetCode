# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        此题相对于求二叉树的最大深度（LC104）而言，需要多加几个条件判断
        当某一结点的左子树为空时，最小深度应该为其右子树的最小深度+1，
        当某一结点的右子树为空时，最小深度应该为其左子树的最小深度+1，
        当某一结点的左右子树均不为空时，最小深度应该为左右子树的最小深度的最小值+1
        """
        if root is None:
            return 0
        if root.left is None:       # 此处实际上包含了左子树为空，右子树为空或者不为空的两种情况
            return self.minDepth(root.right) + 1
        elif root.right is None:    # 左子树不为空，右子树为空
            return self.minDepth(root.left) + 1
        else:                       # 左右子树均不为空
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))