class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Option 2
        length = len(chars)
        i, insert = 0, 0
        count = c = None
        
        while i < length:
            c = chars[i]
            count = 1
            i += 1
            while i < length and chars[i] == c:
                count += 1
                i += 1

            chars[insert] = c
            insert += 1

            if count != 1:
                for n in str(count):
                    chars[insert] = n
                    insert += 1

        return insert

        # Option 1
        """
        def updateCount(chars, i, count):
            for n in str(count):
                chars[i] = n
                i += 1

            return i

        count = 1
        previou = None
        insert = 0
        for i in range(len(chars)):
            if chars[i] == previou:
                count += 1
            else:
                if count != 1:
                    insert = updateCount(chars, insert, count)
                chars[insert] = chars[i]
                previou = chars[i]
                count = 1
                insert += 1

        if count != 1:
            return updateCount(chars, insert, count)

        return insert
        """
