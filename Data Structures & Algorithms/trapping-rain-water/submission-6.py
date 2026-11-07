class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxleft = height[l]
        maxright = height[r]

        res = 0

        while l<r:
            if maxleft < maxright:
                #the last place will overflow with water
                l+=1
                maxleft = max(maxleft , height[l])
                res+=maxleft - height[l]
            else:
                r-=1
                maxright = max(maxright , height[r])
                res+= maxright - height[r]

        return res