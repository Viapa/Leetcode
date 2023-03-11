"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
"""

"""
使用两个栈来解决最小栈问题
第一个栈stack用于存储当前元素
第二个栈min_stack用于存储最小元素和顺序
每次比较min_stack[-1]元素和当前元素val的大小，如果val小于等于前者，则在min_stack继续添加
确保min_stack元素都是按从高到底排序的,每次getMin就是获取min_stack[-1]的元素
"""


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]