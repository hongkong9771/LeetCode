class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = len(fruits)
        if l <= 2:
            return l
        basket = fruits[0:2]
        slow, fast = 0, 2
        res = 2
        while fast < l:
            if fruits[fast] not in basket:
                if len(set(basket)) + 1 > 2:
                    slow = fast - 1
                    while fruits[slow] == fruits[slow-1]:
                        slow -= 1
                basket = [fruits[slow], fruits[fast]]       # 更新篮子内的品种
            tmp = fast - slow + 1                           # 更新可以装下的最大数量
            res = max(res, tmp)
            # print(fruits[slow:fast + 1], basket)
            fast += 1
        return res