# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        二叉搜索树满足根节点严格大于左子树的节点，并且严格小于右子树的节点。
        因此，当给出二叉搜索树的前序遍历之后，第一个元素即为根节点，然后在
        此遍历的序列中找到刚好小于根节点并且刚好大于根节点的两个节点即为左右子树的分隔点

        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        i = 1
        l = len(preorder)
        while i < l:
            if preorder[0] < preorder[i]:
                root.left = self.bstFromPreorder(preorder[1:i])
                root.right = self.bstFromPreorder(preorder[i:])
                break
            elif preorder[0] > preorder[i] and i == l - 1:
                root.left = self.bstFromPreorder(preorder[1:i+1])
                root.right = self.bstFromPreorder([])
            elif preorder[0] > preorder[i] and preorder[0] < preorder[i+1]:
                root.left = self.bstFromPreorder(preorder[1:i+1])
                root.right = self.bstFromPreorder(preorder[i+1:])
                break
            i += 1
        return root