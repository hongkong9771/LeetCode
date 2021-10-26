# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 此题也是建立在二叉树的层次遍历基础上的，相当于将每层的节点值求平均后输出
        res = []
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res.append(sum([node.val for node in queue])/len(queue))
            queue_temp = []
            for node in queue:
                if node.left is not None:
                    queue_temp.append(node.left)
                if node.right is not None:
                    queue_temp.append(node.right)
            queue = queue_temp
        return res