class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 , rob2 = 0 , 0

        for n in nums:
            temp = max(n + rob1 , rob2)
            #[rob1 , rob2 , n , n+1 , n+2 ,.....]
            #so basicaly we can rob either rob1 + n or rob2 then we shift
            #rob1 = rob2 , and rob2 = n that is the end hpusr max which we can rob
            #so everytime we have two choices and we need the last two value max we can rob
            rob1 = rob2
            rob2 = temp
        return rob2
