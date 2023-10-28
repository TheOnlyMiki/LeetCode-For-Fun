class Twitter(object):

    def __init__(self):
        self.users = {}
        self.index = int(1e5)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.users:
            self.users[userId]['t'].append([self.index, tweetId])
        else:
            self.users[userId] = { 'f':{userId}, 't':[ [self.index, tweetId] ] }
        
        self.index -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.users:
            return [ t for _,t in sorted( t for uid in self.users[userId]['f'] for t in self.users[uid]['t'] )[:10] ]

        return []

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.users:
            self.users[followeeId] = { 'f':{followeeId}, 't':[] }
            
        if followerId in self.users:
            self.users[followerId]['f'].add(followeeId)
        else:
            self.users[followerId] = { 'f':{followerId, followeeId}, 't':[] }

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.users:
            self.users[followerId]['f'].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
