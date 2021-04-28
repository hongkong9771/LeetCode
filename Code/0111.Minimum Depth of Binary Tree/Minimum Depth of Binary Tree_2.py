# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        此题相对于求二叉树的最大深度（LC104）而言，在使用层次遍历的迭代法求解时，
        当遇到第一个子节点（即左、右子节点均为空）时，即为最小深度所对应的叶子节点       
        """
        depth = 0
        flag = 0    # 退出循环的标志
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            depth += 1
            queue_temp = []
            for node in queue:
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
                if not node.left and not node.right:
                    flag = 1
                    break
            if flag == 1:
                break
            queue = queue_temp
        return depth