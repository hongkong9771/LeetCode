"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 此题的思路与二叉树的最大深度（LC104题）一样
    # 采用递归的方法，递归的精简版
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1