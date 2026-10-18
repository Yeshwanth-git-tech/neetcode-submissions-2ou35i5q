class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for n in nums:
        #     count[n] = count.get(n , 0) + 1

        # #so key , and value is frequency
        # minheap = []
        # for n, v in count.items():
        #     heapq.heappush(minheap , [v , n])

        # while len(minheap) > k:
        #     heapq.heappop(minheap)
        # res = []
        # for v , n in minheap:
        #     res.append(n)

        # return res


        # count = {}
        # for n in nums:
        #     count[n] = count.get(n , 0) + 1
            
        # ordered = sorted(count , key = lambda n:count[n] , reverse = True)

        # return ordered[:k]

        ##bucket sort

        buckets = [[] for i in range(len(nums)+1)]

        count = {}
        for n in nums:
            count[n] = count.get(n , 0) + 1
       
        for n in count:
            buckets[count[n]].append(n)

    

        #so the highest occuring is at the end
        #as the index is frequency and the number is at its place
        res = []
        for i in range(len(buckets)-1 , 0 , -1):
            for n in buckets[i]:
                res.append(n)
            if len(res) == k:
                return res

        
        