# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = []
        if root is not None:
            queue.append(root)
        
        while len(queue) > 0:
            queue_temp = []
            for node in queue:
                if node.left is not None:
                    queue_temp.append(node.left)
                if node.right is not None:
                    queue_temp.append(node.right)
            if len(queue_temp) == 0:
                break
            queue = queue_temp
        return queue[0].val