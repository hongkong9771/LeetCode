class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            number = nums.count(i)  # 统计重复数字个数
            while number > 1:       # 当数字任然存在重复时，继续删除
                nums.remove(i)
                number -= 1