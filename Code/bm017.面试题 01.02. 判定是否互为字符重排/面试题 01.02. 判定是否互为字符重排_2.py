class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        方法一：逐项减去map
        """

        dict_char1 = dict()

        for char1 in s1:
            dict_char1[char1] = dict_char1.get(char1, 0) + 1
        
        for char2 in s2:
            if char2 in dict_char1:
                dict_char1[char2] = dict_char1[char2] - 1
                if dict_char1[char2] < 0:
                    return False
            else:
                return False
        return True