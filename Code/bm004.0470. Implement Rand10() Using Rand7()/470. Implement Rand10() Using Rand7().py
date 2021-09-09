# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        """
        对于实现从rand10()到rand7()，只需要不断调用rand10()，直至出现1-7中的数即可；
        但是对于rand7()到rand10()，则需要将rand7()映射到一个大于10的数即可，然后再按照大数到小数的不断调用

        生成1~49的数 ：(rand7()-1)*7+rand7()
        首先rand7()-1得到集合 {0,1,2,3,4,5,6}
        然后再乘7，得到集合 {0,7,14,21,28,35,42}
        后面rand7()，得到集合 {1,2,3,4,5,6,7}
        最终得到1~49的数，每个数都是等概率的
        """

        num = (rand7()-1)*7+rand7()
        while num > 10:
            num = (rand7()-1)*7+rand7()
        return num