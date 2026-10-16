class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list) #it will have(time , tweetid)
        self.followmap = defaultdict(set) #set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time , tweetId])
        self.time-=1
        #maxheap

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for t , tid in self.tweetmap[userId]:
            heapq.heappush(heap , [t , tid])

        for f in self.followmap[userId]:
            for t,tid in self.tweetmap[f]:
                heapq.heappush(heap ,[t, tid])

        res = []

        while heap and len(res) < 10:
            t, tid = heapq.heappop(heap)
            res.append(tid)

        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followmap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
