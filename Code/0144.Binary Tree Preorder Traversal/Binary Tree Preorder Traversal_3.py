# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 使用栈的思想进行迭代
        """
        先将根节点（此处的根节点也可指子树中的根节点，不一定是整棵子树的根节点）放入栈中，
        然后将根节点进行出栈操作，接着，按顺序将该根节点的右、左子节点进栈
        """
        # 用于存储最终的结果，
        res = []
        stack = []
        if root:
            stack.append(root)
        cur = root
        while cur and len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
                cur = node.right
            if node.left is not None:
                stack.append(node.left)
                cur = node.left
        return res