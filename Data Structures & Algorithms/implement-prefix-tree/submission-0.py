class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        #intitialize root
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        #start with root
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            #else
            #update the pointer
            curr = curr.children[c]
        return curr.endofword
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        #here we dont need to rech the end of word
        # return curr.endofword
        
        