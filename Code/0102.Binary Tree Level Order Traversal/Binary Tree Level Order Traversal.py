# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 新建一个队列用于存储每一层的树节点
        res = []
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res.append([node.val for node in queue])
            queue_temp = [] # 用于存储每一层的树节点
            for node in queue:
                if node.left is not None:
                    queue_temp.append(node.left)
                if node.right is not None:
                    queue_temp.append(node.right)
            queue = queue_temp
        return res