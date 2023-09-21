# Option 2
import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.small = 1
        self.visit = set()
        self.queue = []

    def popSmallest(self):
        if self.queue:
            self.visit.remove(self.queue[0])
            return heapq.heappop(self.queue)
        
        self.small += 1
        return self.small-1

    def addBack(self, num):
        if num > 0 and self.small > num and num not in self.visit:
            heapq.heappush(self.queue, num)
            self.visit.add(num)
                
# Option 1
"""
class SmallestInfiniteSet(object):

    def __init__(self):
        self.small = 1
        self.queue = set()

    def popSmallest(self):
        while self.small in self.queue:
            self.small += 1

        self.queue.add(self.small)

        return self.small

    def addBack(self, num):
        if num > 0 and num in self.queue:
            self.queue.remove(num)
            if self.small > num:
                self.small = num"""

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
