class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Option 2 - Math Method
        record = []
        for i in range(1, n+1):
            if i % 15 == 0:
                record.append("FizzBuzz")
            elif i % 3 == 0:
                record.append("Fizz")
            elif i % 5 == 0:
                record.append("Buzz")
            else:
                record.append(str(i))

        return record

        # Option 1 - Dynamic Programming Method
        """
        record = ["1", "2", "Fizz", "4", "Buzz"]
        for i in range(5, n):
            count = ""
            if record[i-3][0] == 'F':
                count += "Fizz"
            if record[i-5][0] == 'B' or len(record[i-5]) == 8:
                count += "Buzz"

            record.append(count if count else str(i+1))
            
        return record if n > 4 else record[:n]
        """
