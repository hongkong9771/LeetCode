# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 使用迭代的方法求解
        """
        先序遍历的顺序是中 -> 左 -> 右，改变左右子节点的顺序之后变成，中 -> 右 -> 左，之后反转，顺序就变为左 -> 右 -> 中
        此顺序即为后序遍历的顺序
        先将根节点（此处的根节点也可指子树中的根节点，不一定是整棵子树的根节点）放入栈中，
        然后将根节点进行出栈操作，接着，按顺序将该根节点的左、右子节点进栈
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
            if node.left is not None:
                stack.append(node.left)
                cur = node.left
            if node.right is not None:
                stack.append(node.right)
                cur = node.right
        return res[-1::-1]