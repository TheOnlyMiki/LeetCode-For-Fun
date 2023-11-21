# Option 2 - Array Method
class MyCircularDeque(object):

    def __init__(self, k):
        '''
        :type k: int
        '''
        self.head = self.index = 0
        self.length = k
        self.store = [-1]*k

    def insertFront(self, value):
        '''
        :type value: int
        :rtype: bool
        '''
        if self.isFull():
            return False

        self.head = (self.head-1) % self.length
        self.store[ self.head ] = value
        self.index += 1
        return True

    def insertLast(self, value):
        '''
        :type value: int
        :rtype: bool
        '''
        if self.isFull():
            return False

        self.store[ (self.head + self.index) % self.length ] = value
        self.index += 1
        return True

    def deleteFront(self):
        '''
        :rtype: bool
        '''
        if self.isEmpty():
            return False

        self.store[self.head] = -1
        self.head = (self.head+1) % self.length
        self.index -= 1
        return True

    def deleteLast(self):
        '''
        :rtype: bool
        '''
        if self.isEmpty():
            return False

        self.store[ (self.head + self.index - 1) % self.length ] = -1
        self.index -= 1
        return True

    def getFront(self):
        '''
        :rtype: int
        '''
        return self.store[self.head]

    def getRear(self):
        '''
        :rtype: int
        '''
        return self.store[ (self.head + self.index - 1) % self.length ]

    def isEmpty(self):
        '''
        :rtype: bool
        '''
        return self.index == 0

    def isFull(self):
        '''
        :rtype: bool
        '''
        return self.index == self.length


# Option 1 - Linked List Method
"""
class Node(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque(object):

    def __init__(self, k):
        '''
        :type k: int
        '''
        self.head = self.last = current = Node(val=-1)
        while k != 1:
            current.next = Node(val=-1,prev=current)
            k, current = k-1, current.next

        current.next, self.head.prev = self.head, current

    def insertFront(self, value):
        '''
        :type value: int
        :rtype: bool
        '''
        if self.isFull():
            return False

        if self.head.val != -1:
            self.head = self.head.prev

        self.head.val = value

        return True

    def insertLast(self, value):
        '''
        :type value: int
        :rtype: bool
        '''
        if self.isFull():
            return False

        if self.last.val != -1:
            self.last = self.last.next

        self.last.val = value

        return True

    def deleteFront(self):
        '''
        :rtype: bool
        '''
        if self.isEmpty():
            return False

        self.head.val = -1

        if self.head.next.val != -1:
            self.head = self.head.next

        return True

    def deleteLast(self):
        '''
        :rtype: bool
        '''
        if self.isEmpty():
            return False

        self.last.val = -1

        if self.last.prev.val != -1:
            self.last = self.last.prev

        return True

    def getFront(self):
        '''
        :rtype: int
        '''
        return self.head.val

    def getRear(self):
        '''
        :rtype: int
        '''
        return self.last.val

    def isEmpty(self):
        '''
        :rtype: bool
        '''
        return True if self.head.val == -1 else False

    def isFull(self):
        '''
        :rtype: bool
        '''
        return False if self.last.next.val == -1 else True
"""

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
