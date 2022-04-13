import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        min_heap = []   # 使用最小堆存数组
        res = 1
        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])
        while k > 0:
            min_value = heapq.heappop(min_heap)
            heapq.heappush(min_heap, min_value+1)
            k -= 1
        for i in range(len(min_heap)):
            res = (res* min_heap[i]) % mod      # 如果不每次取余会导致超时
        return res