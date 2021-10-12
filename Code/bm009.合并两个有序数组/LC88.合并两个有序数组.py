class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = len(nums1)
        for i in range(m, l):
            nums1[i] = float('inf')
        i, j = 0, 0
        while i < l and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                i += 1
                j += 1