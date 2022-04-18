class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        令P[i]表示nums[0]至nums[i]之和，sum(i,j)表示nums[i]至nums[j]范围内的子数组之和，可以表示为P[j]-P[i-1]（其中，0<i<j）。题目要求是统计sum(i,j)=k的个数。
        因此，可以在遍历的过程中，构造一个字典用于统计P[i]出现的个数，当P[j]-k在字典中时（其中j>i），统计其出现的次数，即为满足条件的个数，然后继续遍历和累加。
        当然，对于本身和就为k的情况，可以对字典进行初始化，即dict_cnt = {0: 1}
        """
        dict_cnt = {0: 1}
        total = 0
        cnt = 0
        for elem in nums:
            total += elem
            diff = total - k
            tmp = dict_cnt.get(diff, 0)
            cnt += tmp
            dict_cnt[total] = dict_cnt.get(total, 0) + 1
        return cnt
