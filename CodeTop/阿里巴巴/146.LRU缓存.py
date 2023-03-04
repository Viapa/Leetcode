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
6、链表格式: Head -> ^ -> (5,5) -> (3,3) -> (1,1) -> ^ -> tail 
"""

# 定义Node节点类
class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key  # 节点的key
        self.val = val  # 节点的value
        self.next = None  # 后续节点
        self.prev = None  # 前序节点

# 定义LRU缓存类
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity  # 缓存容量
        self.cache = dict()  # 缓存Map, 键为名称key, 值为节点Node
        self.head = Node()  # 初始化头节点
        self.tail = Node()  # 初始化尾节点
        self.head.next = self.tail  # 连接头尾节点
        self.tail.prev = self.head  # 连接头尾节点

    def get(self, key):
        if key not in self.cache:  # 若key不存在于缓存中，返回-1
            print(f"The key: {key} not in cache!")
            return -1
        else:  # 若key存在于缓存，取出对应节点node，将其移动到头部节点位置，然后返回其值
            node = self.cache[key]
            self._move_to_head(node)
            print(f"The key: {key} in cache, with value: {node.val}")
            return node.val

    def put(self, key, value):
        if key not in self.cache:  # 若key不存在于缓存中，新建一个node，并记录于hashMap
            node = Node(key, value)
            self.cache[key] = node
            print(f"Create a new key: {key}")
            self._add_to_head(node)   # 将新节点增加到头部节点（因为也是最新访问）
            if len(self.cache) > self.capacity:  # 判断增加节点后的容量
                del_node = self._pop_tail()   # 如果大于阈值，则删除尾部节点位置的节点
                del self.cache[del_node.key]
                print(f"Remove key: {del_node.key}")
        else:  # 若已存在key，只需要更改value，并将其移动到头部节点位置
            node = self.cache[key]
            node.val = value
            print(f"The key: {node.key} is exists, change value to {value}")
            self._move_to_head(node)

    # 移动某个节点到头部位置
    def _move_to_head(self, node):
        self._remove_node(node)  # 第一步，先删除节点所在位置
        self._add_to_head(node)  # 第二步，添加节点到头部位置

    # 添加某个节点到头部位置
    def _add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    # 去除尾部节点位置的节点
    def _pop_tail(self):
        del_node = self.tail.prev
        self._remove_node(del_node)
        return del_node

    # 去除某个节点
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# 测试功能
if __name__ == "__main__":
    capacity = 3
    LRU = LRUCache(capacity)
    tuples = ((1, 3), (2, 4), (3, 9))
    for (key, value) in tuples:
        LRU.put(key, value)
    out = (8, 8)
    # test1
    LRU.put(out[0], out[1])
    print("------------")
    # test2
    LRU.get(2)
    print("------------")
    # test3
    LRU.put(3, 10)
    LRU.put(20, 10)
