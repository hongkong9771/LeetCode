class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        此题可以参考一下LC53.最大子序和，但是二者又不完全一样，因为子序和只需要满足前面和最大即可。
        而此题为乘积最大，当前面的乘积为负时，后面也有可能遇到一个负数，然后相乘得到最大值，
        因此，在进行动态传递过程中，需要维护两个值：
        一个记录以当前数nums[i]结尾的最大值max_num，其值为：max_num[i] = max(max_num[i-1] * nums[i], min_num[i-1] * nums[i], nums[i])
        另外一个记录以当前数结尾的最小值min_num，其值为：min_num[i] = min(max_num[i-1] * nums[i], min_num[i-1] * nums[i], nums[i])
        每一个以nums[i]结尾的连续子数组的乘积的最大值即为对应的max_num.
        """

        l = len(nums)
        max_num, min_num, res = nums[0], nums[0], nums[0]

        for i in range(1, l):
            mx, mn = max_num, min_num
            max_num = max(mx * nums[i], mn * nums[i], nums[i])
            min_num = min(mx * nums[i], mn * nums[i], nums[i])
            res = max(res, max_num)
        return res