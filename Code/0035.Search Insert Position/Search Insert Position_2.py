class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """二分查找法"""
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return left