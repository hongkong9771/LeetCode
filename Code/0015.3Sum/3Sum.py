class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # 去除掉数组元素小于3个元素的数组
        ans = []
        if n < 3:
            return ans
        nums.sort()
        for k in range(n-2):
            if nums[k] > 0:     # 去除掉最小元素大于0的情况
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue 
            left, right = k+1, n-1
            while left < right:
                s = nums[k] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif s > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    ans.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return ans