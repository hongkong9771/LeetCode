class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        slow, fast = 0, 0
        res = float('inf')
        while slow < l and fast < l:
            if sum(nums[slow:fast+1]) >= target:
                res = min(res, fast-slow+1)
                slow += 1
            else:
                fast += 1
        return res if res != float('inf') else 0