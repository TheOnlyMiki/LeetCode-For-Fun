class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        # Option 2
        if n > goal:
            return 0

        record = {}
        mod = 10**9 + 7

        def getNumMP1(i, song):
            if i == goal:
                return 1 if song == goal else 0

            return (n - song) * getNumMP1(i+1, song+1) % mod

        def getNumMP2(i, song):
            if i == goal:
                return 1 if song == n else 0

            if (i, song) in record:
                return record[(i, song)]

            temp = 0
            if song < n:
                temp += (n - song) * getNumMP2(i+1, song+1)
            if song > k:
                temp += (song - k) * getNumMP2(i+1, song)

            temp %= mod
            record[(i, song)] = temp % mod
            return temp

        if n == goal:
            return getNumMP1(0, 0)
        else:
            return getNumMP2(0, 0)

        # Option 1 - Cannot pass, it was BF method
        """
        if n > goal:
            return 0
            
        self.output = 0
        record = set()
        iteration = range(1, n+1)
        count = { num:0 for num in iteration }
        self.row = []

        def getNumMP1(i):
            if i == goal:
                self.output += 1
                return 

            for n in iteration:
                if n not in record:
                    record.add(n)
                    self.row.append(n)
                    getNumMP1(i+1)
                    self.row.pop()
                    record.discard(n)

        def getNumMP2(i):
            if i == goal:
                for n in iteration:
                    if count[n] == 0:
                        return

                self.output += 1
                return 

            if i > k:
                temp = self.row[i-k-1]
                record.discard(temp)

                for n in iteration:
                    if n not in record:
                        record.add(n)
                        self.row.append(n)
                        count[n] += 1
                        getNumMP2(i+1)
                        count[n] -= 1
                        self.row.pop()
                        record.discard(n)

                record.add(temp)
            else:
                for n in iteration:
                    if n not in record:
                        record.add(n)
                        self.row.append(n)
                        count[n] += 1
                        getNumMP2(i+1)
                        count[n] -= 1
                        self.row.pop()
                        record.discard(n)

        if n == goal:
            getNumMP1(0)
        else:
            getNumMP2(0)

        return self.output
        """
