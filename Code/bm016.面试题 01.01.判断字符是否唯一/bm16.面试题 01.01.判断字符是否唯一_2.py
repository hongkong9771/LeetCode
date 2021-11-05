class Solution:
    def isUnique(self, astr: str) -> bool:
        str_list = set(list(astr))
        return len(astr) == len(str_list)