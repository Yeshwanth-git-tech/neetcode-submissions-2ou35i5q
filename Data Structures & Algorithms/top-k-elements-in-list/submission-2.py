import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # # freq = [[] for i in range(len(nums)+1)]
        # # print(freq)
        # res = []
        # for c in nums:
        #     hashmap[c] = hashmap.get(c , 0) + 1
        
        # for n , c in hashmap.items():
        #     heapq.heappush(res , (c , n) )
        #     if len(res) > k:
        #         heapq.heappop(res)

        # return [num for count , num in res]
        # print(res)

        

        # # for n , c in hashmap.items():
        # #     freq[c].append(n)
        # # print(freq)

         # for i in range(len(freq)-1 , 0 , -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res












        count = {}

        for num in nums:
            count[num] = count.get(num , 0) + 1

        # now we will ahve the count has value and the key is the num

        #SIMILAR TO BUCKET SORT

        # lets create the buckets

        buckets = [[] for i in range(len(nums)+1)]
        #this willl create the buckets

        # now lets add the freq as the index and the num in its place so 
        #if 3 is repeated 3 times it must be in 3rd index

        for n , c in count.items():
            buckets[c].append(n)

        # now lets get the value from topk

        result = []
        for i in range(len(buckets)-1 , 0 , -1):
            for counts in buckets[i]:
                result.append(counts)
                if len(result) == k:
                    return result









        
       