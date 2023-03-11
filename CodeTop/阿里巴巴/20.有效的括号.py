"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""

"""
使用栈来存储左括号，同时用字典存储右括号为key，左括号为value的映射关系
当字符为左括号时，添加到栈中；
当字符为右括号时，若栈空，返回false；
若栈不空，则找到map_dict中对应的左括号，并判断栈顶元素是否与之相同，不同返回false
若相同，pop掉栈顶元素并继续下一个循环
最后栈为空才表示把所有的括号都对应消除了。
"""

def isValid(s):
    map_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                return False
            val = stack.pop()
            if map_dict[c] != val:
                return False

    return stack == []


