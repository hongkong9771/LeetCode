# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        根据以上定义，若root是p, q的最近公共祖先，则只可能为以下情况之一：
        p和q在root的子树中，且分列root的异侧（即分别在左、右子树中）；
        p = root，且q在root的左或右子树中；
        q = root，且p在root的左或右子树中；
        按照先序遍历的方式进行递归查找，直到遇到空的节点或者p、q节点然后递归地返回。
        共有以下四种情况：
        1.当left和right都为空时，则root的左右子树均不包含p、q，返回None
        2.当left和right都不为空时，则p、q分别位于root的左右子树之中，返回root
        3.当left为空，right不为空时，则又分为以下两种情况：
        (1).p、q两节点均位于root的右子树中，此时right即为p、q的最近公共祖先
        (2).p、q其中一个节点位于root的右子树，此时right指向p、q中的一个节点
        4.当right为空时，left不为空时，同第3种情况。
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:  # 情况1
            return None
        if not left:                # 情况3
            return right
        if not right:               # 情况4
            return left
        return root                 # 情况2