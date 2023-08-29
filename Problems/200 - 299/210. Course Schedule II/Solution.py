class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        record = {}

        for course, pre in prerequisites:
            if course in record:
                record[course].append(pre)
            else:
                record[course] = [pre]

        register = set()
        output = []

        def checkCourseBeenTaken(course):
            if course not in record:
                if course not in output:
                    output.append(course)
                return True

            if course in register:
                return False

            register.add(course)

            for pre in record[course]:
                if not checkCourseBeenTaken(pre):
                    return False

            del record[course]
            output.append(course)

            return True

        for course in range(numCourses):
            if not checkCourseBeenTaken(course):
                return []

        return output
