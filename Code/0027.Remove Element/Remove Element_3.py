class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        利用双指针的方法
        分成左右指针，当左指针的值等于val时，将右指针的值赋给左指针，右指针左移一位，
        当左指针的值不等于val时，左指针右移一位。
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
