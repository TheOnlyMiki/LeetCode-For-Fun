class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #number_dict = { num : int(num)**2 for num in "1234567890" }
        number_dict = { 
            '0' : 0,
            '1' : 1,
            '2' : 4,
            '3' : 9,
            '4' : 16,
            '5' : 25,
            '6' : 36,
            '7' : 49,
            '8' : 64,
            '9' : 81,
         }
        count = set([1])

        while n not in count:
            count.add(n)

            consum = 0
            for value in str(n):
                consum += number_dict[value]
            
            n = consum
        
        if n == 1:
            return True
        
        return False
