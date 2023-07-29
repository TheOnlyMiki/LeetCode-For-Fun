class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Option 2
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        
        return True

        # Option 1 
        """
        count_m = {}

        for c in magazine:
            if c in count_m:
                count_m[c] += 1
            else:
                count_m[c] = 1

        for c in ransomNote:
            if c in count_m and count_m[c] > 0:
                count_m[c] -= 1
            else:
                return False

        return True
        """
