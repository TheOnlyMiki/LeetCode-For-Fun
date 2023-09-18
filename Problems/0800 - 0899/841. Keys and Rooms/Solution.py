class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        record = set(rooms[0])
        keys = {i for i in range(1,n)} - record

        while record:
            temp = set()
            for room in record:
                temp |= set(rooms[room]) & keys
            keys -= temp
            record = temp

        return len(keys) == 0
