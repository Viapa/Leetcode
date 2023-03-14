"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
"""

"""
使用栈a来存储入栈元素，栈b来弹出元素
每当pop和peek时，判断栈b是否为空，如果为空就把全部栈a元素依次从头部弹出，压入栈b中，然后弹出栈顶元素，则实现了先进先出
后续继续pop时，如果栈b还不空，说明还可以继续弹出元素，不需要再压入，直到栈b空为止。
因此，判断队列是否空时，需要判断栈a元素和栈b元素是否都空了。
"""


class MyQueue(object):
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x):
        self.stack_a.append(x)

    def pop(self):
        if not self.stack_b:
            while self.stack_a:
                val = self.stack_a.pop()
                self.stack_b.append(val)
        return self.stack_b.pop()

    def peek(self):
        if not self.stack_b:
            while self.stack_a:
                val = self.stack_a.pop()
                self.stack_b.append(val)
        return self.stack_b[-1]

    def empty(self):
        if self.stack_a or self.stack_b:
            return False
        else:
            return True
