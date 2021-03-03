class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        if n < 4:
            return res   # 数组元素个数不满足要求
        for p in range(n-3):                          # 使用while循环也可，但是需要注意p+1，否则极易出现死循环，下面的循环类似
            """判断条件是否满足，不满足则去掉"""    
            if nums[p] + 3 * nums[p+1] > target:      # 数组中不存在满足要求的元素，直接跳出
                break
            if nums[p] + 3 * nums[-1] < target:       # p不满足要求，跳至下一个元素
                continue
            if p > 0 and nums[p] == nums[p-1]:        # 去掉重复的值
                continue
            for k in range(p+1, n-2):                  # 相较于3Sum，在此处多加了一个循环
                if nums[p] + nums[k] + 2 * nums[k+1] > target: # 数组中不存在满足要求的元素，直接跳出
                    break
                if nums[p] + nums[k] + 2 * nums[-1] < target: # k不满足要求，跳至下一个元素
                    continue
                if k > p + 1 and nums[k] == nums[k-1]:            # 去掉重复的值
                    continue
                left, right = k + 1, n - 1
                while left < right:
                    ans = nums[p] + nums[k] + nums[left] + nums[right]
                    if ans == target:
                        res.append([nums[p], nums[k], nums[left], nums[right]])                         # 满足条件，左右指针向中间移动
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:       # 存在重复的数值，左指针继续右移
                            left += 1
                        while left < right and nums[right] == nums[right+1]:     # 存在重复的数值，右指针继续左移
                            right -= 1
                    elif ans > target:                                          # 元素和大于target值，右指针向左移
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:    # 存在重复的数值，右指针继续左移
                            right -= 1
                    else:
                        left += 1                                               # 元素和小于target值，左指针向右移
                        while left < right and nums[left] == nums[left-1]:      # 存在重复的数值，左指针继续右移
                            left += 1
        return res