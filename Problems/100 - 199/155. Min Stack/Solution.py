class MinStack(object):

    def __init__(self):
        self.stack = []
        self.record_min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.record_min_stack:
            self.record_min_stack.append(min(self.record_min_stack[-1], val))
        else:
            self.record_min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.record_min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.record_min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
