class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1
                right += 1
            else:
                right += 1 
        return left + 1
