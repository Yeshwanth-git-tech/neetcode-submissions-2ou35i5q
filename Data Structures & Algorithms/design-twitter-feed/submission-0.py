class Twitter:

    def __init__(self):
        #so that which tweetId was created recently
        self.count = 0
        self.tweetMap = defaultdict(list) #userId : [count , tweetId]
        self.followMap = defaultdict(set) #userId: set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count , tweetId])
        #next tweet created at different count
        #as we use minheap the largest/most recent element is at the top
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        #to get the most recent tweets of the followers and his own
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            #so index is the last value of the list
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count , tweetId = self.tweetMap[followeeId][index]
                #the first value that we are appending will be used as the key
                #index -1 is th eposition we are foing to look in the list of the followeeId , unless it is not empty
                minHeap.append([count , tweetId , followeeId , index -1 ])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count , tweetId , followeeId , index = heapq.heappop(minHeap)
            res.append(tweetId)
            #so we will check if followeeId has any more tweets in this index 
            #redifining the count
            #assuming index is valid , the there are some tweets left for the user
            if index >=0:
                count , tweetId  = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap , [count , tweetId , followeeId , index -1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # if followerId not in self.followMap:
        #     self.followMap[followerId] = set()
        # self.followMap[followerId].add(followeeId)
        #hashset
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
