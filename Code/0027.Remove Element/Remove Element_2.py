class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        利用双指针的方法
        1.i为慢指针，j为快指针；
        2.当nums[j]=val时，j向后移，i不动（i相当于指定与val相等的位置）
        3.当 nums[j]!=val时，将nums[j]的值赋给nums[i]，相当于将后面的值移到i处
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i