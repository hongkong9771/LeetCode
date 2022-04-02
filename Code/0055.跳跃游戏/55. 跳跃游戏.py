class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0        # 用于记录前面所有跳跃中的最远跳跃距离
        for i, jump in enumerate(nums):
            # 如果前面所有跳跃距离未超过当前位置，则说明无法到达后面的位置，则return False
            if max_jump < i:
                return False
            else:
                # 如果前面所有跳跃距离超过了当前位置，则新的最远跳跃距离为原来的跳跃距离max_jump
                # 和当前位置的最远跳跃距离取最大值
                max_jump = max(max_jump, i + jump)
            if max_jump >= len(nums) - 1:
                return True 