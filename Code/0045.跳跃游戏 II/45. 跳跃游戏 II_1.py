class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        i为非负整数数组nums的索引，jump为每一个位置处所能跳跃的最远距离
        思路：对于每一个位置i，其所能跳跃的范围为从位置i开始后的1 ~ jump之间，选择跳至哪一个位置，
        则取决于哪一个位置处的i+jump最大，在每次选取最大i+jump时，同步更新跳跃次数step，记录每次
        跳跃的位置用idx表示。
        """

        n = len(nums)
        MaxPos = 0
        i, step = 0, 0
        idx = 0
        while i < n - 1:
            for j in range(i+1, i+nums[i]+1):       # 位置i处可以跳跃的范围
                if j < n-1:
                    if j + nums[j] > MaxPos:
                        idx = j                     # 取最远跳跃距离的位置i
                        MaxPos = j + nums[j]
                else:
                    return step + 1                 # 当跳跃范围包括最后一个元素时，返回最终的跳跃次数
            i = idx         # 起跳位置
            step += 1
        return 0