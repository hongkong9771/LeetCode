"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 此题在LC102题的基础上，将二叉树变成了N叉树
        res = []
        queue = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            res.append([node.val for node in queue])
            queue_temp = []
            for node in queue:
                if node.children:   # 如果孩子节点存在，就将其全部放置于该层节点处
                    queue_temp.extend(node.children)
                # for child in node.children:
                #     queue_temp.append(child)
            queue = queue_temp
        return res