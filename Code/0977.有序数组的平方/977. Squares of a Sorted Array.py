class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        解题思路：
        数组原本就是有序的，平方后的数组也要求是有序的，其实没有必要求平方后再重新排序，
        因为平方后的最大值必然在原数组上的左右两侧，只需依次比较左右两侧数字平方后的值即可，
        最大的值放在新数组的最后面即可。
        """
        left, right = 0, len(nums) - 1
        square = [0] * len(nums)
        cnt = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                square[cnt] = nums[left] ** 2
                left += 1
            else:
                square[cnt] = nums[right] ** 2
                right -= 1
            cnt -= 1
        return square