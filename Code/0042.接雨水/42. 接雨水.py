class Solution:
    def trap(self, height: List[int]) -> int:
        """
        对于位置i处的柱子，其所能接住的雨水的高度为第i个柱子与其左右两侧最高柱子中的最小值。因此第i个柱子所能接到的雨水为接住雨水的高度减去height[i]。
        对于第i个柱子，我们分别找到包含位置i的左右两侧的柱子的最高值，并用数组记录为leftMax和rightMax
        从左往右遍历，leftMax[i]表示位置i及其左侧中的最高值；
        从右往左遍历，rightMax[i]表示位置i及其右侧中的最高值；
        在计算总的雨水的过程中，从左往右遍历，每个位置i处所接住的雨水为min(leftMax[i], rightMax[i]) - height[i]
        """
        n = len(height)
        leftMax, rightMax = [0]*n, [0]*n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        # 计算leftMax和rightMax
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        res = 0
        for i in range(1, n-1):     # 左右两侧无法接住雨水
            res = res + min(leftMax[i], rightMax[i]) - height[i]
        
        return res