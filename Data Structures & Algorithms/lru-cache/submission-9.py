class Node:
    def __init__(self , key , val):
        self.key , self.val = key , val
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        #hashmap
        self.cache = {}

        #create the lru , mru
        self.left , self.right = Node(0 , 0) , Node(0 , 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self , node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self , node):
        #at the right most
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        node.next = nxt

        prev.next = node
        nxt.prev = node

        
    def get(self, key: int) -> int:
        if key in self.cache:
            #remove from double linked list
            self.remove(self.cache[key])
            #insert at MRU , right most end
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
       
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key , value)
        self.insert(self.cache[key])

        #now check the capacity
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            #key of the nmode to be deleted from hashmap
            del self.cache[lru.key]


        