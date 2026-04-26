class Node:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.cache = {}
        self.left = Node(0 , 0)
        self.right = Node(0 , 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self , node):
        prev = node.prev
        nxt = node.next
        #so the link is changed
        prev.next = nxt
        nxt.prev = prev

    def insert(self , node):
        #because we are going to add near the right most node
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        #now for node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
       

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key , value)
        #dont forget to add it to the linkedlist
        self.insert(self.cache[key])

        #check capacity 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


