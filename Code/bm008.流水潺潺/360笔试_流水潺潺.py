# -*- coding:utf-8 -*-

"""
@Time : 2021/9/25 15:58
@Author : 危红康
@File : 流水潺潺.py
@Software: PyCharm
"""

"""
水从高处往低处流（严格小于），在某一位置处注入水源，使得被注入水的位置最多。求最多被注入水源的个数。
具体地来说，如果当前一个位置i是有水的，并且有某一个相邻的格子j高度严格小于i(hj < hi)，那么j也会成为有水的，
并且i仍然是有水的。对于j相邻的格子也是如此。
nums = [10, 9, 8, 7, 6, 5, 1, 2, 1, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

"""
解题思路:
有两个解题思路，大致思想是一样的，但是就实现手段而言，第二种更容易理解和计算
1.从左往右计算最长连续递增序列的长度为dp_z，
  从左往右计算最长连续递减序列的长度为dp_j，
  将对应的递增值与对应的递减值相加，找出最大的那个值即为最多的水源个数，
  此处的递增对应与递减对应建议画图计算，然后参考代码，逻辑有点复杂，看不懂的话，直接看第二种方法吧。
2.从左往右计算最长连续递增序列的长度为dp_z，
  从右往左计算最长连续递增序列的长度为dp_j，
  将dp_z和dp_j两两对应相加，最大的值即为最终结果。

"""
# n = int(input())
# nums = list(map(int, input().split()))

nums = [10, 9, 8, 7, 6, 5, 1, 2, 1, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums = [5, 1, 2, 1, 5]
n = len(nums)


dp_z = [1] * n      # 最长连续递增序列数组
dp_j = [1] * n      # 最长连续递减序列数组

"""
# 方法一:
for i in range(1, n):
    if nums[i] > nums[i-1]:
        dp_z[i] = dp_z[i-1] + 1
    elif nums[i] < nums[i-1]:
        dp_j[i] = dp_j[i-1] + 1
print(dp_z)
print(dp_j)

res = [1 for _ in range(n)]

result = 1      # 记录最后的结果
for i in range(n):
    res[i-dp_j[i]+1] = max(res[i-dp_j[i]+1], dp_z[i-dp_j[i]+1]+dp_j[i]-1)

    result = max(result, res[i-dp_j[i]+1])
"""

# """
# 方法二:
for i in range(1, n):
    if nums[i] > nums[i-1]:
        dp_z[i] = dp_z[i-1] + 1
for i in range(n-2, -1, -1):
    if nums[i] > nums[i+1]:
        dp_j[i] = dp_j[i+1] + 1
print(dp_z)
print(dp_j)

res = [1 for _ in range(n)]

result = 1      # 记录最后的结果
for i in range(n):
    res[i] = dp_z[i] + dp_j[i] - 1
    result = max(result, res[i])

# """
print(result)






