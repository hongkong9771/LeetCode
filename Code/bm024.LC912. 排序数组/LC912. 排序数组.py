# *-* coding: utf8 *-* 
# @Time : 2021/3/14 20:57
# @Author : 危红康
# @File : whk_sort.py
# @Software: PyCharm


import random


class Sort(object):
    """
    十个经典的排序算法
    1.冒泡排序（Bubble Sort）         //重点
    2.选择排序（Selection Sort）
    3.插入排序（Insertion Sort）
    4.希尔排序（Shell Sort）
    5.归并排序（Merge Sort）          //掌握原理
    6.快速排序（Quick Sort）          //重点
    7.堆排序（Heap Sort）            //掌握原理
    8.计数排序（Counting Sort）
    9.桶排序（Bucket Sort）
    10.基数排序（Radix Sort）
    """

    def Bubble_Sort(self, nums):
        """
        1.冒泡排序
        每次排序之后，最大数会达到序列尾部，小的数会慢慢地向序列头部挪动
        """
        n = len(nums)
        for i in range(n):
            for j in range(1, n-i):         # i可以表示为遍历次数，j表示从头遍历到n-i，因为经历过i次遍历之后，序列尾部的i个值已经被排好序了（放置着最大的值）
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums

    def Selection_Sort(self, nums):
        """
        2.选择排序
        从未排序的序列当中找到最小（大）的元素，并将其与序列头（尾）部元素进行调换，经过一次选择排序后的序列，
        头（尾）部第1个元素已被排列好，之后再从剩下未经排序的序列当中继续找最小（大）的元素，并与当前未排序序列的头（尾）部元素进行调换
        """
        n = len(nums)
        for i in range(n):
            temp = i
            for j in range(i, n):           # 设置下标temp的初始值为i，j从i开始一直往后挪动，当遇到比nums[temp]还小的值时,将temp的值更新为j。
                if nums[temp] > nums[j]:
                    temp = j
            nums[i], nums[temp] = nums[temp], nums[i]
        return nums

    def Insertion_Sort(self, nums):
        """
        3.插入排序
        默认第1位元素已经排好序，接着从第2位开始在已排好序的序列中，从后往前扫描，找到相应位置并插入，以此类推。
        """
        n = len(nums)
        for i in range(n-1):
            j = i + 1
            while j > 0 and nums[j] < nums[j-1]:        # 第i+1个元素在已排好序的序列（0~i）中从后往前扫描，找到相应位置并插入。
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums

    def Shell_Sort(self, nums):
        """
        4.希尔排序
        又称缩小增量排序，以gap为增量，将序列以gap为间隔分成n//gap个序列，对n//gap个序列分别进行插入排序，
        之后将gap缩小至gap//2，再次进行分割序列和排序操作，直至gap为0
        """
        n = len(nums)
        gap = n // 2
        while gap:      # while循环的时间复杂度为log2n
            for j in range(0, gap):             # 用于遍历以gap为间隙的组数，一共gap组，需遍历gap次
                for i in range(j, n, gap):      # 以gap为间隙，遍历每组，使用插入排序法进行排序，共需遍历n/gap次，结合上一个for循环，两个for循环的时间复杂度为O(n)
                    while i >= gap and nums[i - gap] > nums[i]:
                        nums[i - gap], nums[i] = nums[i], nums[i - gap]
                        i -= gap
            gap //= 2
        return nums

    def Merge_Sort(self, nums):
        """
        5.归并排序
        归并排序，采用是分治法，先将数组分成子序列，让子序列有序，再将子序列间有序，合并成有序数组。
        """

    def Quick_Sort_1(self, nums):
        """
        6.快速排序
        递归版本：Quick_Sort
        先随机选择一个中间值pivot做为基准，比这个pivot小的放到左边，大的放到右边
        """
        n = len(nums)

        def quick_sort(left, right):
            if left >= right:
                return nums
            index = random.randint(left, right)
            pivot = nums[index]
            nums[left], nums[index] = nums[index], nums[left]
            i, j = left, right
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            # nums[i] = pivot
            quick_sort(left, i-1)
            quick_sort(i+1, right)
            return nums
        return quick_sort(0, n-1)

    """
    非递归版本：Quick_Sort_2
    使用栈去存储每次待排序的区间索引
    """
    # 非递归版本快排
    # 单次区间排序
    def quick_sort(self, left, right, nums):
        index = random.randint(left, right)
        pivot = nums[index]
        nums[left], nums[index] = nums[index], nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] > pivot:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        return i    # 分割区间的索引


    def Quick_Sort_2(self, nums):
        n = len(nums)
        s = []
        s.extend([0, n-1])
        while s:
            right = s.pop()
            left = s.pop()
            if left >= right:
                continue
            else:
                mid = self.quick_sort(left, right, nums)
                s.extend([left, mid-1])
                s.extend([mid+1, right])
        return nums
        
    def Heap_Sort(self, nums):
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


if __name__ == "__main__":
    nums = [23, 56, 3, 34, 12, 1, 13]
    # nums = [5, 2, 3, 1]
    # nums = [1]
    s = Sort()
    print("原始数组: ", nums)
    # 冒泡排序
    # nums_bubble_sort = s.Bubble_Sort(nums)
    # print("冒泡排序后的数组: ", nums_bubble_sort)

    # 选择排序
    # nums_selection_sort = s.Selection_Sort(nums)
    # print("选择排序后的数组: ", nums_selection_sort)

    # 插入排序
    # nums_insertion_sort = s.Insertion_Sort(nums)
    # print("插入排序后的数组: ", nums_insertion_sort)

    # 希尔排序
    # nums_shell_sort = s.Shell_Sort(nums)
    # print("希尔排序后的数组: ", nums_shell_sort)

    # 快速排序
    # nums_quick_sort = s.Quick_Sort_2(nums)
    # print("快速排序后的数组: ", nums_quick_sort)

    # 堆排序
    nums_heap_sort = s.Heap_Sort(nums)
    print("堆排序后的数组: ", nums_heap_sort)