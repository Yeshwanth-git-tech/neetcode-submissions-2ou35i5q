class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            #when the value on top of queue is lesser than nums[r]
            #we pop
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            #then we are allowed to add the new value
            q.append(r)
            #if our left value is out of window length 
            #if our left index is greater than left most index value of our queue
            if l > q[0]:
                q.popleft()

            #our window is atleast size k , to update the ouput
            if (r - l + 1 ) >=k:
                #leftmostvalue
                output.append(nums[q[0]])
                #update pointer
                #once our window is atleast size k
                l+=1
            r+=1

        return output