# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 采用队列迭代的方法解决，两两对应取节点，每次判断一组（两个）节点的值是否相同
        queue = []
        if not root:
            return True
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) > 0:
            left_node = queue.pop(0)
            right_node = queue.pop(0)
            if not left_node and not right_node:    # 左、右节点均为空，此时说明是对称的
                continue
            if not left_node or not right_node or left_node.val != right_node.val:  # 左、右节点有一个不为空，或者左、右节点都不为空，但值不相等
                return False
            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)
        return True