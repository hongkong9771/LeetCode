class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        令P[i]表示nums[0]至nums[i]之和，则每个连续子数组之和sum(i,j)就可以写出成P[j]-P[i-1](0<i<j)的形式，此时，判断子数组的和是否能被k整除就等价于判断(P[j]-P[i-1]) % k == 0，根据同余定理，只要P[j] % k == P[i-1] % k，就可以保证式子成立。
        因此，在遍历数组的过程中，统计以i结尾的数组的和P[i]对k取余结果一样的个数（余数为键，个数为值），这样，当新的的P[j]对k取余结果出现在之前的字典中时，取出其所对应的值a，则新增加的满足条件的个数为k。依此类推，一边遍历一边求满足条件的子数组的个数
        对于P[i] % k = 0的情况，其本身就满足条件，因此，对于0作为键的情况，还需初始化其为1
        """
        dict_cnt = {0: 1}
        total = 0
        cnt = 0
        for num in nums:
            total += num
            mod = total % k
            tmp = dict_cnt.get(mod, 0)
            cnt += tmp
            dict_cnt[mod] = tmp + 1
        return cnt