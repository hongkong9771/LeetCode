class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        list_S = list(S)
        for i in range(len(S)):
            if list_S[i] == " ":
                list_S[i] = "%20"
        list_S = list_S[:length]
        s = "".join(list_S)
        return s