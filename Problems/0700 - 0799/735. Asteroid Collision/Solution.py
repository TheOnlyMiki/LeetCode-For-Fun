class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        def checkCollision(asteroid):
            while stack and stack[-1] >= 0:
                temp = asteroid + stack[-1]
                if temp < 0:
                    stack.pop()
                elif temp > 0:
                    return True
                else:
                    stack.pop()
                    return True

            return False

        stack = []
        for asteroid in asteroids:
            if asteroid < 0 and checkCollision(asteroid):
                continue

            stack.append(asteroid)

        return stack
