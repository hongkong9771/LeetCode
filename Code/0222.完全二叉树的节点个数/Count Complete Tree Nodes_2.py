# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 采用层次遍历的迭代方式
        num = 0
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            num += len(queue)
            queue_temp = []
            for node in queue:
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
        return num