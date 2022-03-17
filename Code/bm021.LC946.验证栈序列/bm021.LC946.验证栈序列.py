"""
对于给定的入栈字符和出栈字符，判断是否可以完成完整的入栈出栈操作。
例如
pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
pushed为需要入栈的元素，poped为需要出栈的元素，
求是否可以通过对pushed进行入栈操作，对poped进行出栈操作，
使得一个空栈经过上述操作之后仍为空栈

示例1:
pushed:
1 2 3 4 5
popped:
1 2 3 4 5
5 4 3 2 1
2 3 4 5 1
4 1 2 3 5

示例2:
pushed:
A B C D E F
popped:
D E F C B A (True)
D C E F B A (True) 
F E D C B A (True)
F E C D B A (False)
A B C D E F (True)
A D C B F E (True)


"""


def stackoperate(pushed, popped):
    l1 = len(pushed)
    l2 = len(popped)
    stack = []
    i, j = 0, 0
    while i < l1 or j < l2:
        while i < l1:
            stack.append(pushed[i])
            i += 1
            if stack[-1] == popped[j]:
                break
        while j < l2:
            if stack != [] and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                break
        if i == l1 and j < l2:
            return False
        elif i == l1 and j == l2:
            return True


pushed = list(input().split(" "))
popped = list( input().split(" "))


res = stackoperate(pushed, popped)
print(res)