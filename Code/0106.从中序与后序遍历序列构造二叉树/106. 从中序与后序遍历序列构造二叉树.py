# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        中序遍历左、中、右，后序遍历为左、右、中
        对于二叉树的序列[1, 2, 3, 4, 5, 6, 7], 那么其前序遍历为 [4, 2, 5] + [1] + [6, 3, 7]，而后序遍历为 [4, 5, 2] + [6, 7, 3] + [1]
        如果知道根节点的位置，就可以对这些数组进行分组（分成左右子树），并用递归生成树的每个分支
        首先，根节点必然在后序遍历中的最后一位，在中序遍历中，根节点将左右子树分隔开，即根节点的左侧即为左子树，右侧即为右子树
        接下来就可以将根节点的左右子树的中序遍历以及后序遍历分别输入到原函数中进行递归调用
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        
        ind = inorder.index(postorder[-1])      # 在中序遍历中的位置，同时也是左子树的长度
        root.left = self.buildTree(inorder[0:ind], postorder[0:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        return root