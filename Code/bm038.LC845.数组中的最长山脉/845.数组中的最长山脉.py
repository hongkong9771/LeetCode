class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        分别找到每一个位置上左右两侧的连续递增和递减子数组的长度left[i], right[i]，然后针对当前位置而言，其最长山脉子数组的长度即为left[i]+right[i]+1
        """
        n = len(arr)
        if n < 3:
            return 0
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0
        
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        
        res = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:        # 此处的判断很重要
                res = max(res, left[i] + right[i] + 1)

        return res