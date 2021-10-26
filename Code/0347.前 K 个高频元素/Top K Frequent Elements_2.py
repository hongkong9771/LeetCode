import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素出现的频率
        map_count = dict()
        for i in range(len(nums)):
            map_count[nums[i]] = map_count.get(nums[i], 0) + 1
        
        # 定义一个小顶堆
        min_heap = []
        # 小顶堆弹出的元素为最小元素
        for key, freq in map_count.items():
            heapq.heappush(min_heap, (freq, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = [0] * k
        for i in range (k-1, -1, -1):
            res[i] = heapq.heappop(min_heap)[1]
        
        return res