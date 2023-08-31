# Option 2 - Using two heap to store the smaller(max heap) and grather(min heap) numbers 
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []

    def addNum(self, num):
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small,-num)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Option 1 - binary search method for finding index
'''
class MedianFinder(object):

    def __init__(self):
        self.length = 0
        self.store = []
        self.target = None

    def findIndex(self, left, right):
        if self.store[right-1] <= self.target:
            return right

        mid = temp = None
        while left <= right:
            mid = (left + right) // 2
            temp = self.store[mid]
            if self.target < temp:
                right = mid-1
            elif self.target > temp:
                left = mid+1
            else:
                return mid

        return left

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.store:
            self.target = num
            i = self.findIndex(0, self.length)
            self.store.insert(i, num)
        else:
            self.store.append(num)
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        left, right = self.length/2, (self.length-1)/2
        return (self.store[left] + self.store[right]) / 2.0
'''

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
