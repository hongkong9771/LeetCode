# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        前序遍历为中、左、右，中序遍历为左、中、右
        对于二叉树[3, 9, 20, null, null, 15, 7]而言，其前序遍历为[3, 9, 20, 15, 7]，中序遍历为[9, 3, 15, 20, 7]
        由前序遍历可知perorder[0]（即列表中的元素3）为根节点，根据preorder[0]可以在中序遍历中确定左右子树，
        这是因为根节点将左右子树分隔开来，因此，可以根据左右子树的长度确定前序遍历中的左右子树
        """

        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        # 确定左子树长度
        ind = inorder.index(preorder[0])       # 在中序遍历中的位置，同时也是左子树的长度
        root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return root