class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for n in stones:
            heapq.heappush(res , -1 * n)
        
        while len(res) > 1:
            stone1 = -1*heapq.heappop(res)
            stone2 = -1*heapq.heappop(res)

            newstone = stone1 - stone2

            heapq.heappush(res , -1*newstone)

        return -1*res[0] if res else 0




        