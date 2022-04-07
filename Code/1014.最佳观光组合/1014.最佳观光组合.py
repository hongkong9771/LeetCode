class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        因为最高得分表示为res = values[i] + values[j] + i - j，因此，可以将其拆分为两个部分：
        values[i]+i和values[j]-j
        即对每个A[j]而言，要使得res最大，则是要求A[i]+i(i<j)最大，因此，对于A[j]而言，前面取最大的A[i]+i，遍历完所有的j，即可得到最大观光评分
        """
        n = len(values)
        res = 0
        MaxPre = values[0] + 0
        
        for j in range(1, n):
            res = max(res, values[j] - j + MaxPre)
            MaxPre = max(MaxPre, values[j] + j)
        return res