class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        首先对数组中的所有值进行异或操作，最后得到的值即为要求的两个元素的异或值，接着对异或值进行分析：
        两个数异或，则相同为0，不同为1。因此，剩余两个数的异或结果中必然有1，则1对应的位置在两个元素中
        分别为0和1，根据此位置是否为0或1，可以将元素组分成两个数组，这样可以将两个元素分开，并且相同的
        元素必然在同一个数组中。两个数组分别异或，即可分别得到两个只出现一次的元素
        不能把整数直接变成二进制再找1的位置，因为python中的bin(num)对会省略掉前面多余的0，导致判断1的
        位置有误。
        """
        ans = 0
        for num in nums:
            ans ^= num
        
        index = 1
        while index & ans == 0:
            index <<= 1
        
        res1, res2 = 0, 0
        for num in nums:
            if index & num == 0:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]
