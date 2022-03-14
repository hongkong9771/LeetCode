class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 以此代码为准

        slow, fast = 0, 1

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow + 1