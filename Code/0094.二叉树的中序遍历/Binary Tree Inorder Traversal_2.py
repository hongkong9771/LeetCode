# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 借助于栈，使用迭代法解决
        """
        首先将根节点添加入栈中，然后将根节点的左子节点（如果有的话）添加入栈中，直至最后一个左子节点，
        之后，执行出栈操作，并判断该节点的右子节点是否存在，若存在，则继续按照上面的步骤将节点进行入栈操作，
        若不存在，则继续执行出栈操作，如此循环。
        """
        res = []
        stack = []
        cur = root
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                cur = node.right
            else:
                cur = None
        return res