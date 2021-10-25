# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 采用递归方式调用
        if root is not None:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res