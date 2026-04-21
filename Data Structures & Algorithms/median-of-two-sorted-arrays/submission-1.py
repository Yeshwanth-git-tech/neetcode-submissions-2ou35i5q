class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m = sorted(nums1 + nums2)

        
        # if len(m) % 2 == 0:
        #     a = len(m)//2 
        #     b = len(m)//2 - 1
        #     print(a)
        #     print(m[a], m[b])
        #     print(b)
        #     median = (m[a]+m[b])/2
        #     return median
        # else:
        #     return m[len(m)//2]

        # #so this is brute force O(m+n)

        A  , B = nums1 , nums2

        total = len(A) + len(B)

        half = (len(A) + len(B)) // 2

        if len(B) < len (A):
            A , B = B , A

        l = 0

        r = len(A) - 1

        while True:
            #first find the in small list
            i = (l+r) // 2
            j = half - i - 2
            #basically the list exist the len will be greater than
            #i >=0 , it can be length of 1
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                #check if it is odd first
                #if total exist , after mod
                if total%2: 
                    return min(Aright , Bright)
                #dont forget , this else condition within if condtion
                else:
                    print(max(Aleft , Bleft))
                    print(min(Aright , Bright))
                    return (max(Aleft , Bleft) + min(Aright , Bright)) / 2

            #and then this becomes elif
            # if Aleft > Bright:
            elif Aleft > Bright:
                r  = i -1
            else:
                l = i+1

