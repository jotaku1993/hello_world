class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk = []
        self.dct = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.stk.append([tweetId, userId])
        if userId not in self.dct:
            self.dct[userId] = [userId]
        else:
            if userId not in self.dct[userId]:
                self.dct[userId].append(userId)
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        #print self.stk
        #print self.dct
        if userId not in self.dct:
            return []
        member = self.dct[userId]
        ans = []
        l = len(self.stk)
        idx = l-1
        while len(ans) <= 10:
            if idx == -1:
                break
            if self.stk[idx][1] in member:
                ans.append(self.stk[idx][0])
            idx -= 1
        if len(ans) == 10:
            return ans
        else:
            return ans[:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.dct:
            self.dct[followerId] = [followeeId]
        else:
            if followeeId not in self.dct[followerId]:
                self.dct[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId not in self.dct:
            return
        else:
            if followeeId in self.dct[followerId]:
                self.dct[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
