# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        对于每一个树节点，我们都可以选择偷与不偷两个状态，最终盗取的最高金额即为二者中的最大值
        选择后序遍历的原因是需要先计算中间节点的值，在递归中，后序遍历中间节点是先遍历的。
        """
        value = self.rob_tree(root)
        return max(value[0], value[1])
    

    def rob_tree(self, node):
        if node is None:    # 遍历到空节点时，返回0
            return (0,0)    # (不偷当前节点，偷当前节点)
        
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[0] + right[0]    # 偷当前节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点
        return (val2, val1)