class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        maxPos为最远跳跃距离，end为位置i处的最远跳跃范围的右边界，当i跳跃到边界处时，跳跃步数加1，
        这种方式 是以跳跃范围作为计数器，每走完一个跳跃范围，则step+1。
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0     
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step