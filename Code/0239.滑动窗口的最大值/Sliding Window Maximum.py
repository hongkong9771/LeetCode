from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()     # 双端队列，既可以左端出列，也可以右端出列
        res = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue and queue[0] == i-k:
                queue.popleft()
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res