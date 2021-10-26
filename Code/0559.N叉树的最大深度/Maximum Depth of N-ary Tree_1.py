"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 此题的思路与二叉树的最大深度（LC104题）一样
    # 采用递归的方法
    def maxDepth(self, root: 'Node') -> int:
        return self.getDepth(root)
    
    def getDepth(self, node):
        if node is None:
            return 0
        depth = 0
        for child in node.children:
            depth = max(depth, self.getDepth(child))
        return depth + 1