class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        7.堆排序
        先建立一个最大堆（最大堆的定义为：树的顶点元素为整个数组的最大值，所有父节点的元素均大于其子节点），
        这样最大的元素就处于堆顶，即整个数组中的第1位，然后将第1位的元素与最后1位相调换，则最大元素就在最后面了
        （有点类似选择排序）。这样，最后一个元素就是有序的了，后面的所有操作均不包含最后一个有序的元素，接下来调整堆，
        使其满足最大堆，然后再将堆顶元素与倒数第二个元素交换，则最后两个元素就是有序的了。以此类推，最终获得有序数组。

        其中，使用数组存储堆时，有这样一条规则：以第i个元素为父节点的左右子节点在数组中的索引分别为：
        left = 2 * i + 1
        right = 2 * i + 2

        注：可参考此链接：https://zhuanlan.zhihu.com/p/124885051
        """
        def adjust_heap(nums, node, n):
            left = node * 2 + 1
            if left < n:
                right = left + 1
                if right < n and nums[left] < nums[right]:
                    left = right
                if nums[node] < nums[left]:
                    nums[left], nums[node] = nums[node], nums[left]
                    """
                    递归调用
                    进行父节点与左右最大子节点之间的调换后，还需让调换后的
                    left继续与其子节点进行判断，以确保满足最大堆的条件
                    """
                    adjust_heap(nums, left, n)

        # 建立最大堆
        n = len(nums)
        for node in range(n // 2, -1, -1):
            adjust_heap(nums, node, n)
        # 调整堆
        for i in range(n-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            """
            只需调整树的根节点处的元素与其子节点即可（当然，如果该父节点的子节点变动了，
            则仍需递归地调用其子节点，adjust_heap已经写好了）满足最大堆。
            """
            adjust_heap(nums, 0, i)
        return nums



