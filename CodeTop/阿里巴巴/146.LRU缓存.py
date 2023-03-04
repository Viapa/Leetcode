"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""

"""
解题思路：
1、首先需要一个哈希表来记录键值对，key为名，value是node类节点。
2、还需要一个双向链表来记录访问顺序。
3、当访问一个键时，如果它存在于哈希表中，则将其移到双向链表的头部，表示它最近被使用过。
4、当插入一个新键值对时，如果缓存已满，则删除双向链表的尾部节点，并从哈希表中删除相应的键值对。然后在双向链表的头部插入新节点，并在哈希表中添加相应的键值对。
5、双向链表的头部节点表示最近使用的节点，尾部节点表示最近最少使用的节点。
"""
# 定义Node节点类
class Node:
    def __init__(self, key=None, val=None):
        self.key = key  # 节点名
        self.val = val  # 节点值
        self.prev = None  # 前序节点
        self.next = None  # 后续节点


# 定义本题的LRU-Cache类
class LRUCache(object):
    # 初始化类变量
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity  # 缓存表容量值
        self.cache = dict()  # 哈希表（字典），用于记录缓存的键值对
        self.head = Node()  # 初始化头部节点
        self.tail = Node()  # 初始化尾部节点
        self.head.next = self.tail  # 头节点的next指向尾节点
        self.tail.prev = self.head  # 尾节点的prev指向头节点, 形成双向链表

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:  # 加入缓存中不存在key，返回-1
            print("This key is not exists")
            return -1
        else:  # 若key存在，则将其对应的节点移动到双向链表的头部，并返回value值
            node = self.cache[key]
            self._move_to_head(node)
            print(f"The key: {key} is exists, with value {node.val}")
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:  # 假设该key已经在缓存中，那就更新节点值，并且将节点移动到链表头部
            node = self.cache[key]
            node.val = value  # 更新节点值
            self._move_to_head(node)  # 移动到头部
        else:  # 假设不存在该key，新建一个node，判断此时的缓存表大小，并将存于链表尾部的节点删除并删除相应key
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)  # 同样移动到头部
            if len(self.cache) > self.capacity:  # 判断容量
                tail_node = self._pop_tail()  # 删除尾部节点
                del self.cache[tail_node.key]
                print(f"Old key: {tail_node.key} is deleted..")
            print(f"New key: {key} is cached..")

    # 将已经存在的节点移动到链表头部
    def _move_to_head(self, node):
        self._remove_node(node)  # 先删除该节点
        self._add_to_head(node)  # 再在链表头部添加该节点

    # 删除一个节点的操作
    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev  # 注意，两侧都要相连才能形成双向链表

    # 将节点移动到头部
    def _add_to_head(self, node):
        node.prev = self.head  # 将头部节点放到该节点的前置
        node.next = self.head.next  # 将该节点的下一个节点为头部节点的下一个节点
        self.head.next.prev = node  # 头部节点下一个节点前置为该节点
        self.head.next = node  # 头部节点的下一个节点为该节点 （这四部就是完全将头部节点替换为node节点）

    # 删除尾部节点
    def _pop_tail(self):
        node = self.tail.prev  # 取尾部节点的前一个节点并删除，实际上是保持了尾部节点不动
        self._remove_node(node)
        return node


# 测试
if __name__ == "__main__":
    capacity = 3
    LRU = LRUCache(capacity)
    tuples = ((1, 3), (2, 4), (3, 9))
    for (key, value) in tuples:
        LRU.put(key, value)
    out = (8, 8)
    # test1
    LRU.put(out[0], out[1])
    # test2
    LRU.get(2)