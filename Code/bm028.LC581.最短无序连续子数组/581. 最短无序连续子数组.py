class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        先只考虑中段数组，设其左边界为L，右边界为R：
        nums[R] 不可能是【L，R】中的最大值（否则应该将 nums[R] 并入右端数组）
        nums[L] 不可能是【L，R】中的最小值（否则应该将 nums[L] 并入左端数组）
        很明显:
        【L，R】中的最大值 等于【0，R】中的最大值，设其为 max
        【L，R】中的最小值 等于【L， len(nums)-1】中的最小值，设其为 min
        那么有：
        nums[R] < max < nums[R+1] < nums[R+2] < ... 所以说，从左往右遍历，最后一个小于max的为右边界
        nums[L] > min > nums[L-1] > nums[L-2] > ... 所以说，从右往左遍历，最后一个大于min的为左边界
        """
        l = len(nums)
        Max, Min = nums[0], nums[l-1]
        left, right = 0, -1
        for i in range(l):
            if nums[i] < Max:
                right = i
            else:
                Max = nums[i]
            j = l-1-i
            if nums[j] > Min:
                left = j
            else:
                Min = nums[j]
        return right - left + 1