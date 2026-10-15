class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #so basic case

        count_p = {}

        for i in s1:
            count_p[i] = count_p.get(i , 0) + 1

        need = len(count_p)

        have = 0

        window = {}
        l=0

        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r] , 0) + 1

            if s2[r] in count_p and count_p[s2[r]] == window[s2[r]]:
                have+=1

            if r-l+1 == len(s1):
                if have == need:
                    return True

                #if it does not match then 
                if s2[l] in count_p and count_p[s2[l]] == window[s2[l]]:
                    have-=1
                window[s2[l]] -= 1 
                l+=1
        return False

            
  

        #we will have two lists

        #we will take the s1 and check that fixed window size first
    
        #we will check if s1 exists in s2 , target is s1 , window valid is window
      

        #if we are not able to find the valid windlow lets go from k , len(s2)
        #we have found the target string values 
   
            # window[ord(s2[i-k]) - ord("a")] +=1
            #we are decrementing the count
            
        # “O(n) time, where n is the length of s2. Each comparison is a fixed 26, so it’s constant.”




        