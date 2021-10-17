import heapq
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        l = len(arr)
        cnt = dict()
        for i in range(l):
            cnt[arr[i]] = cnt.get(arr[i], 0) + 1
        
        min_heap = []   # 维护一个小顶堆，小顶堆弹出的元素为最小的元素
        for key, value in cnt.items():
            heapq.heappush(min_heap, (key, value))
        
        num = 0
        res = []
        for i in range(len(cnt)):
            key, value = heapq.heappop(min_heap)
            num += value
            res.extend([key] * value)
            if num >= k:
                break
        return res[:k]