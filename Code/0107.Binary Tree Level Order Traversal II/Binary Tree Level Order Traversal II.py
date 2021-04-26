# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 相较于二叉树的层序遍历（LC第102题）而言，本题的结果就是将之前的结果反转即可
        res = []
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res.append([node.val for node in queue])
            queue_temp = []
            for node in queue:
                if node.left is not None:
                    queue_temp.append(node.left)
                if node.right is not None:
                    queue_temp.append(node.right)
            queue = queue_temp
        return res[::-1]