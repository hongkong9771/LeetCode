class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        L = list()
        if sum(nums) < target:
            return 0
        while right <= len(nums):
            if sum(nums[left:right+1]) < target:
                right += 1
            else:
                L.append(right+1-left)
                if left == right:
                    right += 1
                    continue
                left += 1
        return min(L)