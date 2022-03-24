# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        前序遍历为中、左、右，后序遍历为左、右、中
        对于二叉树的序列[1, 2, 3, 4, 5, 6, 7], 那么其前序遍历为 [1] + [2, 4, 5] + [3, 6, 7]，而后序遍历为 [4, 5, 2] + [6, 7, 3] + [1]
        如果知道根节点的左子树有多少个节点，就可以对这些数组进行分组，并用递归生成树的每个分支
        假设左子树有L个节点，我们知道左子树的根节点为preorder[1]（也可能无左子树，但是题目要求取多种答案中的一种，
        所以可以假设有左子树），并且其也在后序遍历中左子树的最后，即左子树包含的节点为[4, 5, 2], 
        所以左子树的长度为: L = postorder.index(preorder[1]) + 1
        接下来就可以将根节点的左右子树的前序遍历以及后序遍历分别输入到原函数中进行递归调用
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # 确定左子树的长度
        L = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:L+1], postorder[0:L])
        root.right = self.constructFromPrePost(preorder[L+1:], postorder[L:-1])
        return root