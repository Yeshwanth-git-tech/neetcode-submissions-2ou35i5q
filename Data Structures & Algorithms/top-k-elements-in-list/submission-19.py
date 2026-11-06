class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]

        count = {}

        for n in nums:
            count[n] = count.get(n , 0)+1
        
        for n , c in count.items():
            buckets[c].append(n)

        res = []
        for i in range(len(buckets)-1 , -1 , -1):
            for x in buckets[i]:
                res.append(x)
                if len(res) == k:
                    return res

        