class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    在第i个数的后面判断是否存在满足条件的数target-nums[i]
    """
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return i, nums.index(target-nums[i], i+1)
                
