class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l < 3:
            return False
        left, right = 0, l-1
        while left < l-1:
            if arr[left] < arr[left+1]:
                left += 1
            else:
                break
        while right > 0:
            if arr[right] < arr[right-1]:
                right -= 1
            else:
                break
        return left == right and left != 0 and right != l-1