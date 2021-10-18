# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        queue = []
        cnt = 1
        if root:
            queue.append(root)
        while len(queue) > 0:
            if cnt % 2 == 1:
                res.append([node.val for node in queue])    # 奇数层顺序放入
            else:
                res.append([node.val for node in queue[-1::-1]])    # 偶数层倒序放入
            queue_temp = []
            for node in queue:
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
            cnt += 1
        return res