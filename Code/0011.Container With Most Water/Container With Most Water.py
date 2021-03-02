class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        container = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            container = max(container, min(height[i], height[j]) * (j - i))
        return container