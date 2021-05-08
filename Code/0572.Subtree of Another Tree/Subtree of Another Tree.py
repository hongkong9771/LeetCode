# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, root, subRoot):       # 判断以root和subRoot为节点的两棵子树是否相同
        if not root and not subRoot:
            return True
        elif not root or not subRoot or root.val != subRoot.val:
            return False
        tree_left = self.compare(root.left, subRoot.left)
        tree_right = self.compare(root.right, subRoot.right)
        return tree_left and tree_right

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 比较两棵子树是否相同，若不相同则继续比较以s子节点为根节点的子树，直至比较完毕。
        if not root:
            return False
        if self.compare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)