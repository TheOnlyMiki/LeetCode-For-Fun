# Option 2 - Double Linked List
class Node(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):
    def __init__(self):
        self.index = 0
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def get(self, index):
        '''
        :type index: int
        :rtype: int
        '''
        if index >= self.index:
            return -1

        #print("get", index)
        #self.read()

        if index <= self.index // 2:
            current = self.head.next
            while index != 0:
                index, current = index-1, current.next
        else:
            current = self.tail
            while index != self.index:
                index, current = index+1, current.prev

        return current.val

    def addAtHead(self, val):
        '''
        :type val: int
        :rtype: None
        '''
        self.index += 1
        temp = self.head.next
        self.head.next = Node(val, temp, self.head)
        temp.prev = self.head.next

        #print("head")
        #self.read()

    def addAtTail(self, val):
        '''
        :type val: int
        :rtype: None
        '''
        self.index += 1
        temp = self.tail.prev
        self.tail.prev = Node(val, self.tail, temp)
        temp.next = self.tail.prev

        #print("tail")
        #self.read()

    def addAtIndex(self, index, val):
        '''
        :type index: int
        :type val: int
        :rtype: None
        '''
        if index > self.index:
            return

        #print("add", index, self.index)
        #self.read()

        if index <= self.index // 2:
            current = self.head
            while index != 0:
                index, current = index-1, current.next

            temp = Node(val, current.next, current)
            current.next.prev, current.next = temp, temp
        else:
            current = self.tail
            while index != self.index:
                index, current = index+1, current.prev

            temp = Node(val, current, current.prev)
            current.prev.next, current.prev = temp, temp

        self.index += 1

        #print("after add")
        #self.read()

    def deleteAtIndex(self, index):
        '''
        :type index: int
        :rtype: None
        '''
        if index >= self.index:
            return

        #print("delete", index, self.index)
        #self.read()

        if index <= self.index // 2:
            current = self.head
            while index != 0:
                index, current = index-1, current.next

            current.next.next.prev, current.next = current, current.next.next
        else:
            current = self.tail.prev
            while index != self.index:
                index, current = index+1, current.prev

            current.next.next.prev, current.next = current, current.next.next

        self.index -= 1
        
        #print("after delete")
        #self.read()

    """def read(self):
        current = self.head.next
        output = []
        while current:
            output.append(current.val)
            current = current.next

        print(output)"""


# Option 1 - Single Linked List
"""
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.index = 0
        self.head = Node()

    def get(self, index):
        '''
        :type index: int
        :rtype: int
        '''
        if index >= self.index:
            return -1
        
        current = self.head.next
        while index != 0:
            index, current = index-1, current.next

        return current.val

    def addAtHead(self, val):
        '''
        :type val: int
        :rtype: None
        '''
        self.index += 1
        self.head.next = Node(val, self.head.next)

    def addAtTail(self, val):
        '''
        :type val: int
        :rtype: None
        '''
        self.index += 1
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(val)

    def addAtIndex(self, index, val):
        '''
        :type index: int
        :type val: int
        :rtype: None
        '''
        if index > self.index:
            return

        self.index += 1
        current = self.head
        while index != 0:
            index, current = index-1, current.next

        current.next = Node(val, current.next)

    def deleteAtIndex(self, index):
        '''
        :type index: int
        :rtype: None
        '''
        if index >= self.index:
            return

        self.index -= 1
        current = self.head
        while index != 0:
            index, current = index-1, current.next

        current.next = current.next.next
        """


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
