class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list) #[count , tweetid]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count , tweetId])
        #tweetmap[1].append([0, 5])
#         count = -1

# tweetmap = {1: [[0, 5]]}
# count = -1

# postTweet(2, 6)
# pythontweetmap[2].append([-1, 6])
# count = -2

# tweetmap = {
#     1: [[0, 5]],
#     2: [[-1, 6]]
# }
# count = -2
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        #O(10 * k) , k - number of people that user follows
        #in min heap it is O(10*logk)

        res = []
        minheap = []

        self.followmap[userId].add(userId)

        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                #now we are going to that index in [count , tweet]
                index = len(self.tweetmap[followeeId]) - 1 #the last index position
                count , tweetid =  self.tweetmap[followeeId][index]
                minheap.append([count , tweetid , followeeId , index-1])

        heapq.heapify(minheap)

        while minheap and len(res) < 10:
            count , tweetid , followeeId , index = heapq.heappop(minheap)
            res.append(tweetid)

            if index>=0:
                count , tweetid = self.tweetmap[followeeId][index]
                heapq.heappush(minheap , [count , tweetid , followeeId , index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
