from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        temp = t-3000

        while self.queue and self.queue[0] < temp:
            self.queue.popleft()

        self.queue.append(t)

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
