import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # freq = [[] for i in range(len(nums)+1)]
        # print(freq)
        res = []
        for c in nums:
            hashmap[c] = hashmap.get(c , 0) + 1
        
        for n , c in hashmap.items():
            heapq.heappush(res , (c , n) )
            if len(res) > k:
                heapq.heappop(res)

        return [num for count , num in res]
        print(res)

        

        # for n , c in hashmap.items():
        #     freq[c].append(n)
        # print(freq)


        
        # for i in range(len(freq)-1 , 0 , -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
