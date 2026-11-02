class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time , tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for t , tid in self.tweetmap[userId]:
            heapq.heappush(heap , [t , tid])

        # for f in self.followmap:
        for f in self.followmap[userId]:
            for t , tid in self.tweetmap[f]:
                heapq.heappush(heap , [t , tid])

        res =[]
        #check first heap exits
        # while heap and len(heap) > 10:
        # while len(heap) > 10:
        while heap and len(res) < 10:
            t , tid = heapq.heappop(heap)
            res.append(tid)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)