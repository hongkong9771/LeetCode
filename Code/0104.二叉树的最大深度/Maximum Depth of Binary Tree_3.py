# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        采用迭代的思想，和层次遍历的思想一样，每次遍历一层的节点，树的层数即为根节点的深度
        """
        res = 0
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:   # 判断当层是否包含节点
            res += 1
            queue_temp = []  # 存储每一层的节点
            for node in queue:
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
        return res