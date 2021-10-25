class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []


        def backtrack(n, k, startIndex):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path[:])
                return
            

            for i in range(startIndex,min(9, n)+1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res