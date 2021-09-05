class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        """
        使用异或，异或的规则是相同为0，不同为1，任何数和0异或均为自己本身
        """
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers