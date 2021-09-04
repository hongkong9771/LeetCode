class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        """
        交换a,b的值
        a = a + b
        b = a - b
        a = a - b
        """
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers