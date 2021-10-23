class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = nums.count(val)
        while n > 0:
            nums.remove(val)
            n -= 1