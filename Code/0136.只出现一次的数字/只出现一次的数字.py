class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for i in nums:
            temp ^= i
        return temp
        # return sum(set(nums))*2-sum(nums)