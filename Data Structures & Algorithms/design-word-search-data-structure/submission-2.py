class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            #update the pointer
            curr = curr.children[c]

        curr.word = True
        

    def search(self, word: str) -> bool:
        # curr = self.root
        # UnboundLocalError: cannot access local variable 'curr' where it is not associated with a value connat access it , spo curr shoudl be declared inside the dfs
        def dfs(j , root):
            curr = root #thats why when you call , ylou give self.root
            # for i in range(len(word)):
            for i in range(j , len(word)):
            ##you have to start from theab in .ab , so j , len(word)
                c = word[i]
                if c == ".":
                    #we are skipping the "." and going to its child
                    #because the "." can be anything from a-z
                    for child in curr.children.values():
                        # j , root (now root is child)
                        #i+1 as to skip the "."
                        #if this is true
                        if dfs(i+1 , child):
                             return True
                        
                        #else we did not find match
                    # #this false should be outside the for loop , so all the children are checked    
                    # So for "do.." with "dog" stored, when you reach ".", you try the first child only. If that recursive path returns False, you immediately return False without checking other children.
                    return False

                else:
                    #apple
                    if c not in curr.children:
                        return False
                    #update the pointer
                    curr = curr.children[c]
            return curr.word

        return dfs(0 , self.root)


        
