class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        """
        queue1用于出栈，queue2用于存储栈元素
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) == 1:
            return self.queue1.pop()
        else:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            temp = self.queue1.pop()
            while len(self.queue2) > 0:
                self.queue1.append(self.queue2.pop(0))
        return temp


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1] 


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1) == 0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()