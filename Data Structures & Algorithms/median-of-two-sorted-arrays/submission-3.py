class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A,B = nums1 , nums2
        else:
            A,B = nums2 , nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        # we will do binary search on the small list

        l = 0
        r = len(A) - 1

        while True:
            i = (l+r)//2
            #dont forget to -2
            # j = total - i - 2
            #it half of i-2
            j = half - i - 2

             
            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")
            #correct partition
            if Aleft<=Bright and Bleft <= Aright:
                #now lets get median 
                #check odd or even
                if total%2:
                    return min(Aright , Bright)

                else:
                    return (max(Aleft , Bleft) + min(Aright , Bright) )/ 2

            else:
                if Aleft > Bright:
                    r = i-1
                else:
                    l = i+1


