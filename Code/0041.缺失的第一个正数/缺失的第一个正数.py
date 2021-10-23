class Solution:
    def firstMissingPositive(self, nums) -> int:
        """给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。"""
        # 进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

        length = len(nums)
        i = 0
        for i in range(1, length + 1):
            if i not in nums:
                return i
        return i + 1