"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 此题的思路与二叉树的最大深度（LC104题）一样
    # 采用和层次遍历一样的迭代方法
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        queue = [] 
        if root is not None:
           queue.append(root)
        while len(queue) > 0:
            res += 1
            queue_temp = []
            for node in queue:
                for child in node.children:
                    # if child: 
                    # 若child为空，则添加进去的节点也为空，相当于未添加，所以此处也可以不用判断
                    queue_temp.append(child)
            queue = queue_temp
        return res