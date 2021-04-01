class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []        # 用于出栈时，作辅助栈使用

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 压栈
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 出栈
        if self.empty() == True:        # 若队列为空，则返回空，无法执行出栈
            return
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # 查询队列的第一个元素
        if self.empty() == True:        # 若队列为空，则返回空，无法查询元素
            return
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) + len(self.stack2) == 0:
            return True 
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()