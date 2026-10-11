class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #so basic case
        k = len(s1)

        if len(s1) > len(s2):
            return False

        #we will have two lists
        target = [0] * 26
        window = [0] * 26
        #we will take the s1 and check that fixed window size first
        for i in range(k):
            target[ord(s1[i]) - ord("a")]+=1
            window[ord(s2[i]) - ord("a")]+=1
        #we will check if s1 exists in s2 , target is s1 , window valid is window
        if window == target:
            return True

        #if we are not able to find the valid windlow lets go from k , len(s2)
        #we have found the target string values 
        for i in range(k, len(s2)):
            window[ord(s2[i]) - ord("a")] +=1
            # window[ord(s2[i-k]) - ord("a")] +=1
            #we are decrementing the count
            window[ord(s2[i-k]) - ord("a")] -=1

            if window == target:
                return True
        return False




        