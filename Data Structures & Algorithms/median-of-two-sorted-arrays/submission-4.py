class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A , B = nums1 , nums2
        else:
            A, B  =  nums2 , nums1

        print(A)
        print(B)

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True:
            m = (l+r) // 2
            j = half - m - 2
            
            Aleft = A[m] if m>=0 else float("-infinity")
            Aright = A[m+1] if (m+1)< len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            print("Aleft" , Aleft , "Bleft" , Bleft , "Ar" , Aright , "Br" , Bright)

            if Aleft <= Bright and Bleft <= Aright:
                #partition is correct
                #now odd , even 
                if total%2:
                    #because we know the left side is going to small anyways
                    return min(Aright , Bright)
                else:
                    return (max(Aleft , Bleft) + min(Aright , Bright)) / 2
            else:
                if Aleft > Bright:
                    r = m-1
                elif Bleft > Aright:
                    l = m+1


    