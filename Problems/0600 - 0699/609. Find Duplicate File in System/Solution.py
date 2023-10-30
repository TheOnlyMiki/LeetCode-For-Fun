class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        record = {}
        for path in paths:
            path = path.split(' ')
            for filename in path[1:]:
                index = filename.index('(')
                word = filename[index+1:-1]
                if word in record:
                    record[word].append(path[0] + '/' + filename[:index])
                else:
                    record[word] = [path[0] + '/' + filename[:index]]

        return [ items for items in record.values() if len(items) > 1 ]
