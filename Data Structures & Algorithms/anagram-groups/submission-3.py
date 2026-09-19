from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        

        #base case

        # if len(strs) == 1:
        #     return list(strs)
       
        ##brute force way is sorted which give n*mlogm , m is the average length of string
        # group = {}

        # for s in strs:
        #     key = ''.join(sorted(s))
        #     if key not in group:
        #         group[key] = []
        #     group[key].append(s)

        # return list(group.values())

        # group = defaultdict(list)
        # ##straightforward
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     group[key].append(s)
            
        # return list(group.values())


        ##more efficient

        groups = {}
        #this should be inside the loop , for every word you get new values of list, 
        #that is used as key
        # count = [0] * 26 

        for s in strs: #n len of list strs
            count = [0] * 26
            for c in s: #m average length of each str
                count[ord(c) - ord("a")] +=1
                #list are mutable which cannot be keys , so tuple is immutable
                #this should be outside for loop as , count is calcualted , can be accessed outside this for loop 
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)
                # if tuple(count) not in groups:
                #     groups[tuple[count]] = []
                # groups[tuple[count]].append(s)

        # print(groups.values)
        return list(groups.values())
        




        





         #key is going to be count anfstring such len of 26 - tuple (1 , 0 , 1 ...., 0)
        # value is the string itself in a list
        # hashmap = {}


        


