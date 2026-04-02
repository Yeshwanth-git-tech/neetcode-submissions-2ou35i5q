class Node:
    def __init__(self , key , val):
        self.key , self.val = key , val
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        #lru , most recent
        self.left , self.right = Node(0,0) , Node(0,0)
        #double linked list , we will be inserting and removing
        #between these two nodes
        self.left.next , self.right.prev = self.right , self.left
    
    def insert(self , node):
        prev , nxt = self.right.prev , self.right
        prev.next  = nxt.prev = node
        node.prev , node.next = prev , nxt

    def remove(self , node):
        prev ,nxt = node.prev , node.next
        #if None
        if prev: prev.next = nxt 
        if nxt: nxt.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.cache:
            #remove and insert it to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            self.remove(self.cache[key])
        
        
        #adding to hashmap
        self.cache[key] = Node(key , value)
        #now pointing the pointer from hashmap to node , #inserting
        self.insert(self.cache[key])

        #check capacity
        if len(self.cache) > self.cap:
            #remove lru
            #the left most node
            lru = self.left.next
            self.remove(lru)
            #del from hashmap
            del self.cache[lru.key]
        
