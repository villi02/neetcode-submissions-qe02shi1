class Twitter:

    def __init__(self):
        self.following = {} # key: follower, value: followees[]
        self.followedBy = {} # key: followee, value: followers[]
        self.tweetsBy = {} # key: userId, value: tweets[]
        self.feeds = {} # key: userId, value: mostRecentTweets[] (heap)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # iterate and update all the followers feeds
        self.order += 1
        tweet = (self.order, tweetId, userId)
        if userId in self.tweetsBy:
            self.tweetsBy[userId].append(tweet)
        else:
            self.tweetsBy[userId] = []
            self.tweetsBy[userId].append(tweet)
        
        if userId in self.followedBy: # update followedBy heaps
            for follower in self.followedBy[userId]:
                if follower not in self.feeds:
                    self.feeds[follower] = []
                    self.feeds[follower].append(tweet)
                else:
                    heapq.heappush(self.feeds[follower], tweet)
                    if len(self.feeds[follower]) > 10:
                        heapq.heappop(self.feeds[follower])
        
        # Also authors own
        if userId not in self.feeds:
            self.feeds[userId] = []
            self.feeds[userId].append(tweet)
        else:
            heapq.heappush(self.feeds[userId], tweet)
            if len(self.feeds[userId]) > 10:
                heapq.heappop(self.feeds[userId])


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.feeds:
            return [tweet[1] for tweet in sorted(self.feeds[userId], reverse=True)]
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {}
        if followeeId in self.following[followerId]:
            return
        self.following[followerId][followeeId] = True
        
        
        if followeeId not in self.followedBy:
            self.followedBy[followeeId] = {}
        self.followedBy[followeeId][followerId] = True
        
        # Update the feed of the user
        if followerId not in self.feeds:
            self.feeds[followerId] = []
            heapq.heapify(self.feeds[followerId])
        
        for nextTweet in self.tweetsBy.get(followeeId, [])[-10:]:
            heapq.heappush(self.feeds[followerId], nextTweet)
            if len(self.feeds[followerId]) > 10:
                heapq.heappop(self.feeds[followerId])
        return


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                del self.following[followerId][followeeId]
                del self.followedBy[followeeId][followerId]
            else:
                return
        else:
            return
        
        # Update feed
        if followerId in self.feeds:
            self.feeds[followerId] = []
            for userId in [followerId, *self.following[followerId]]:
                for tweet in self.tweetsBy.get(userId, [])[-10:]:
                    heapq.heappush(self.feeds[followerId], tweet)
                    if len(self.feeds[followerId]) > 10:
                        heapq.heappop(self.feeds[followerId])

        return                
        
