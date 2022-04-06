class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        一共分为以下两种情况：
        1) 不成环时，即最大和的子数组不是环状的；最大子数组和即为maxSum
        2) 成环时，即最大和的子数组一部分在尾部，一部分在首部。最大子数组和即为total-minSum
         max(pre+pro)
        =max(总和-subarray)
        =总和-min(subarray)
        total为数组的总和，maxSum为最大子数组和，dp_max为包含当前整数的最大子数组和；
        minSum为最小子数组和，dp_min为包含当前整数的最小子数组和。
        """
        n = len(nums)
        total = 0
        maxSum, dp_max = nums[0], 0
        minSum, dp_min = nums[0], 0

        for i in range(n):
            dp_max = max(dp_max+nums[i], nums[i])           # 更新包含当前整数的最大子数组和
            maxSum = max(dp_max, maxSum)                    # 更新最大子数组和
            dp_min = min(dp_min+nums[i], nums[i])           # 更新包含当前整数的最小子数组和
            minSum = min(dp_min, minSum)                    # 更新最小子数组和
            total += nums[i]
        
        # 当所有元素全为负数时
        if maxSum <= 0:
            return maxSum
        else:
            return max(maxSum, total-minSum)