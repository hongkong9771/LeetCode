class Solution:
    def mySqrt(self, x: int) -> int:
        left, ans, right = 0, 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans