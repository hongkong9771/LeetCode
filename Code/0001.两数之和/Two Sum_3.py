class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # target-nums[i]在字典里，则返回两个值的索引，若不在，则将nums[i]加入到字典中。
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable.keys():
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []