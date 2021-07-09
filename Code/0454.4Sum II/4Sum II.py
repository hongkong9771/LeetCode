class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 定义一个哈希表，用于存储A和B元素相加的结果出现的次数
        count_AB = dict()
        ans = 0     # 满足条件的元组个数
        for a in nums1:
            for b in nums2:
                count_AB[a+b] = count_AB.get(a+b,0) + 1 # 统计a+b出现的次数
        
        for c in nums3:
            for d in nums4:
                if -(c+d) in count_AB.keys():
                    ans += count_AB[-(c+d)]
        
        return ans
