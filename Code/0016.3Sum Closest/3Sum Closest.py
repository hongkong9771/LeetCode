class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return None
        ans = float("inf")      # 定义一个无穷大的初始值ans
        nums.sort()
        for k in range(0, n-2):
            if (k > 0 and nums[k-1] == nums[k]):    # 去掉重复的值
                continue
            left, right = k+1, n-1
            while left < right:
                s = nums[k] + nums[left] + nums[right]
                if s == target:
                    return s
                if abs(s - target) < abs(ans - target):  # 每移动一次比较一次值
                    ans = s
                if s > target:
                    right -= 1
                else:
                    left += 1
        return ans