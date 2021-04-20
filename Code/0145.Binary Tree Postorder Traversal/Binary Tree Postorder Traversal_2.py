# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 使用迭代的方法求解
        res = []
        stack = []
        while stack or root:
            # 找到左边最下面的叶子节点
            while root:
                stack.append(root)
                if root.left is not None:
                    root = root.left  
                else:
                    root = root.right
            root = stack.pop()
            res.append(root.val)
            if stack and stack[-1].left == root:    # 当栈为非空，且当前节点为左子节点
                root = stack[-1].right              # 接着遍历右子树
            else:               # 当前节点为右子节点时，直接遍历其根节点
                root = None     
        return res