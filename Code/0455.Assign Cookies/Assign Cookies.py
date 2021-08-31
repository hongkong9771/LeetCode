class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        我们优先考虑将大尺寸的饼干分发给大胃口的值，这样才能保证尽可能多的孩子会得到满足，
        首先，对孩子的胃口值和饼干尺寸进行排序，然后对应分发。

        """
        if len(s)== 0:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        for i in range(len(g)):
            if res < len(s) and g[i] <= s[res]:     # 需要判断res < s的数组长度，否则会出现数组角标越界
                res += 1
        return res