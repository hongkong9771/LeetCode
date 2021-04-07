class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    先去掉重复的数字，然后统计每个数字的个数，排序。
    """
        l = list(set(nums))
        a = []
        b = []
        for i in l:
            a.append(nums.count(i))
        for _ in range(k):
            b.append(l[a.index(max((a)))])
            a[a.index(max(a))] = 0
        return b