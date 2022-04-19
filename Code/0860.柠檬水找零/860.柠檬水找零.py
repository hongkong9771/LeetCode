class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        设计一个字典money_cnt统计各种面值钞票出现的次数
        1.当收到5元时，直接5元面值个数加1
        2.当收到10元时，5元面值个数减1，10元面值个数加1
        3.当收到20元时，若有10元，则先用10元；若无10元，则用5元。
        """
        money_cnt = dict()

        for money in bills:
            if money == 5:
                money_cnt[5] = money_cnt.get(5, 0) + 1
            elif money == 10:
                cnt_5 = money_cnt.get(5, 0)
                if cnt_5 == 0:
                    return False
                else:
                    money_cnt[5] = cnt_5 - 1
                    money_cnt[10] = money_cnt.get(10, 0) + 1
            elif money == 20:
                cnt_5 = money_cnt.get(5, 0)
                cnt_10 = money_cnt.get(10, 0)
                if cnt_5 == 0:
                    return False
                if cnt_10 == 0:
                    if cnt_5 < 3:
                        return False
                    else:
                        money_cnt[5] = cnt_5 - 3
                if cnt_10 != 0:
                    money_cnt[5] = cnt_5 - 1
                    money_cnt[10] = cnt_10 - 1
        return True

