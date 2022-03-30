class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        用字典存储每个数组中每个整数出现的次数，然后两两之间进行比较
        """
        dic1 = dict()
        dic2 = dict()
        res = []
        for i in range(len(nums1)):
            dic1[nums1[i]] = dic1.get(nums1[i], 0) + 1
        for i in range(len(nums2)):
            dic2[nums2[i]] = dic2.get(nums2[i], 0) + 1
        
        for key, value in dic1.items():
            if key in dic2:
                num = value if value < dic2[key] else dic2[key]         # 取出现次数的最小值
                res.extend([key] * num)
        return res