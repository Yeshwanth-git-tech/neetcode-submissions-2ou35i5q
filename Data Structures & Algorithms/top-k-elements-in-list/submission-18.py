class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]

        count = Counter(nums)

        for n , c in count.items():
            buckets[c].append(n)

        # print(buckets)

        #so basically im storing the frequency at that index of that array
        res = []
        for i in range(len(buckets)-1 ,0 , -1):
            for x in buckets[i]:
                res.append(x)
                if len(res) == k:
                    return res
            