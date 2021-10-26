# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 使用深度优先搜索
        def construct_path(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:        # 当该节点即为叶子节点时
                    paths.append(path)
                else:
                    path += '->'
                    construct_path(root.left, path)
                    construct_path(root.right, path)

        paths = []          # 存储所有的路径
        construct_path(root, '')
        return paths