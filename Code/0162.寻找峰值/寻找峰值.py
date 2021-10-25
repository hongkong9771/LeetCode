class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        i = 0
        res = []
        
        while i < l:
            if i == 0:
                if nums[i] > nums[i+1]:
                    res.append(i)
                    i += 2
                else:
                    i += 1
            elif i == l - 1:
                if nums[i] > nums[i-1]:
                    res.append(i)
                    i += 2
                else:
                    i += 1
            else:
                if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                    res.append(i)
                    i += 2
                else:
                    i += 1
        return res[0]