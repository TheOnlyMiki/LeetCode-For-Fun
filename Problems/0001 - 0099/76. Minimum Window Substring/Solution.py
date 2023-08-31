class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Option 2
        t_len = len(t)
        s_len = len(s)
        
        count = {}
        # Counting the characters in t
        for c in t:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        i, i_2 = 0, 0
        window_size = s_len + 1
        record_i = 0

        while i_2 < s_len:
            c = s[i_2]
            # Check the char is in t, if in t, we can reduce the number of needs
            if c in count:
                if count[c] > 0:
                    t_len -= 1
                count[c] -= 1

            # If the number of needs to match were 0, means t is find in s
            while t_len == 0:
                # Update window_size when record size is grather then new size
                if window_size > i_2 - i + 1:
                    window_size = i_2 - i + 1
                    record_i = i

                c_2 = s[i]
                # Move i pointer forward, to reduce the window size
                if c_2 in count:
                    if count[c_2] == 0:
                        t_len += 1
                    count[c_2] += 1

                # Initical next iteration
                i += 1

            # Initical next iteration
            i_2 += 1

        if window_size > s_len:
            return ""

        return s[record_i : record_i + window_size]

        # Option 1 - Run time too over, can't pass
        """
        t_len = len(t)
        s_len = len(s)

        i = 0
        window_size = s_len + 1
        record_index = [0, 0]

        while i < s_len:
            if s[i] in t:
                temp = s[i:i+window_size]
                record = []
                try:
                    for c in t:
                        record.append(temp.index(c))
                        temp = temp.replace(c, ' ', 1)
                except:
                    i += 1
                    continue
                
                record = sorted(record)
                new_window_size = record[-1] - record[0] + 1
                if new_window_size < window_size:
                    if new_window_size == t_len:
                        return s[record[0] + i : record[-1] + i + 1]
                    window_size = new_window_size
                    record_index[0] = record[0] + i
                    record_index[1] = record[-1] + i + 1
            
            i += 1

        if window_size > s_len:
            return ""

        return s[record_index[0]:record_index[1]]
        """
