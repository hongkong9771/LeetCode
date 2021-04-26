# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 使用迭代方法求解
        res = []
        stack = []
        while root or len(stack) > 0:
            # 先添加根节点，然后找到最左端最下面的叶子节点
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                node = stack.pop()
                root = node.right
        return res