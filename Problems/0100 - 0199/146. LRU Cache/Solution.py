class ListNode(object):
    def __init__(self, key=0, val=0, next=None, previou=None):
        self.key = key
        self.val = val
        self.next = next
        self.previou = previou 

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_length = capacity
        self.nodes = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.previou = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodes:
            temp = self.nodes[key].val
            address = self.nodes.pop(key)
            address.previou.next = address.next
            address.next.previou = address.previou
            del address

            self.nodes[key] = ListNode(key, temp, self.tail, self.tail.previou)
            self.tail.previou.next = self.nodes[key]
            self.tail.previou = self.nodes[key]
            return temp
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodes:
            address = self.nodes.pop(key)
            address.previou.next = address.next
            address.next.previou = address.previou
            del address
        else:
            if len(self.nodes) == self.max_length:
                address = self.nodes.pop(self.head.next.key)
                self.head.next = address.next
                address.next.previou = self.head
                del address

        self.nodes[key] = ListNode(key, value, self.tail, self.tail.previou)
        self.tail.previou.next = self.nodes[key]
        self.tail.previou = self.nodes[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
