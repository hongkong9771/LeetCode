# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sortedcontainers import SortedList

"""
假设有一个二叉搜索树，模型的根节点为root，树上的节点值均不重复。
初始时，所有节点均为蓝色。现在按顺序对这棵二叉树进行若干次操作，
ops[i] = [type, x, y]表示第i次操作为：
1) type等于0时，将节点值范围在[x, y]的节点均染蓝
2) type等于1时，将节点值范围在[x, y]的节点均染红

请返回完成所有染色后，该二叉树中红色节点的数量

思路：
    按照中序遍历，得到二叉搜索树的所有树节点（已经排好序的），然后构造排序列表res(SortedList)，
    使用res.irange(x, y)可以得到res中范围在(x, y)之间的所有值，并返回一个列表对象。接着反向遍
    历操作（最后一个操作中的范围的树节点的颜色必然与最后一个操作的0|1对应，若为0，则为蓝色；
    若为1，则为红色。）
    因此，
    1）若最后一个操作为红色，则将这些树节点的个数加在colored（用于记录红色树节点的个数）上，
    并将这些树节点全部删除（因为这些树节点最后必然为红色）；
    2）若最后一个操作为蓝色，则无需加在colored上，只需并将这些树节点全部删除（因为这些树节点
    最后必然为蓝色）；
    遍历完所有的操作即可。返回最后的colored值。

"""
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        res = []
        def it(node):
            if node is None:return 
            it(node.left)
            res.append(node.val)
            it(node.right)
        it(root)
        res = SortedList(res)           # 排序列表（res为一个对象）
        colored = 0
        for t,x,y in reversed(ops):     # 反向遍历
            rem = list(res.irange(x,y))
            if t==1:
                colored += len(rem)
            for p in rem:
                res.remove(p)
        return colored