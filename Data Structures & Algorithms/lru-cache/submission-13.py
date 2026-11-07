class Node:
    def __init__(self , key , val , next=None , prev = None):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self , node):
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv

    def insert_node(self ,node):
        nxt = self.right
        prv = self.right.prev

        node.next = nxt
        node.prev = prv

        prv.next = node
        nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key , value)
        self.insert_node(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            # self.remove(self.cache[lru])
            self.remove(lru)
            del self.cache[lru.key]
