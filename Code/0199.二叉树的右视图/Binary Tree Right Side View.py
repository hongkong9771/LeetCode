# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 相较于LC第102题而言，本题是在层序遍历的基础上，保留每一层的最后一个树节点
        res = []
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res.append(queue[-1].val)   # 只保留每层的最后一个树节点
            # res.append([node.val for node in queue)
            queue_temp = []
            for node in queue:
                if node.left is not None:
                    queue_temp.append(node.left)
                if node.right is not None:
                    queue_temp.append(node.right)
            queue = queue_temp
        return res
        # Res = []
        # for r in res:
        #     Res.append(r[-1])
        # return Res

