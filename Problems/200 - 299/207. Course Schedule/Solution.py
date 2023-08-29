class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        record = {}
        for course, pre in prerequisites:
            if course in record:
                record[course].append(pre)
            else:
                record[course] = [pre]

        register = set()

        def checkCourseBeenTaken(course):
            # If the course is not planning to take, then no matter
            if course not in record:
                return True

            # If the course already been taken, it means conflict
            if course in register:
                return False

            # If the course has no conflict then register/taken
            register.add(course)

            # Check the pre require courses is conflict or not (And register when we check)
            for pre in record[course]:
                if not checkCourseBeenTaken(pre):
                    return False

            # If the course and pre require courses all register, then clear the whole list from record
            del record[course]

            return True

        for course in range(numCourses):
            if not checkCourseBeenTaken(course):
                return False

        return True
