# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        采用递归的方式解决，此题与LC第101题类似，一个是判断树是否对称，只需先分别比较左右子节点的外侧，再比较内测即可，
        而此题则是直接比较对应位置处的节点
        """
        # 递归
        def compare(p, q):
            if p is None and q is None:
                return True
            elif not p or not q or p.val != q.val:      # p和q只有一个为空，或者二者都不为空，但是值不相等
                return False
            Tree_left = compare(p.left, q.left)
            Tree_right = compare(p.right, q.right)
            Tree_union = Tree_left and Tree_right
            return Tree_union
        
        return compare(p, q)