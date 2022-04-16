

"""
思路：
    将所有满足条件的料理全部放入，然后统计满足饱腹感的美味度，并取最后最大的美味度。

"""

class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        res = []
        x = 0
        y = 0
        n = len(cookbooks)
        def backtrack(materials, x, y, startIndex):
            # 满足饱腹感的条件，加入res
            if y >= limit:
                res.append(x)
                # return

            for i in range(startIndex, n):
                flag = 0    # 满足条件时，将Flag置为1
                for j in range(5):
                    if materials[j] >= cookbooks[i][j]:
                        flag += 1
                    else:
                        break
                if flag == 5:
                    x += attribute[i][0]
                    y += attribute[i][1]
                    for j in range(5):
                        materials[j] -= cookbooks[i][j]
                    backtrack(materials, x, y, i + 1)
                    for j in range(5):
                        materials[j] += cookbooks[i][j]
                    x -= attribute[i][0]
                    y -= attribute[i][1]
                else:
                    continue

        backtrack(materials, x, y, 0)
        if len(res) == 0:
            return -1
        return max(res)
