class ListNode:
    # 创建双向链表的类
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部节点和伪尾部节点
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过哈希表定位，在移动到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果key不存在，则创建一个新的节点
            node = ListNode(key, value)
            # 并将此node添加进cache
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，则删除双向链表的尾部节点
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            # 将此node移动至双向链表的头部
            node.value = value
            self.moveToHead(node)
            
    # 将node节点移动至双向链表的头部
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    # 在双向链表的头部添加一个节点
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # 删除双向链表中的一个节点
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 删除双向链表尾部的节点
    def removeTail(self):
        # 方法一
        # self.tail.prev.prev.next = self.tail
        # self.tail.prev = self.tail.prev.prev
        # 方法二
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)