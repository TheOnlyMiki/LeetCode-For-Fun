class Solution:
    def myPow(self, x, n):
        return 1.0 / self.pow(x, -n) if n < 0 else self.pow(x, n)
    
    def pow(self, x, n) :
        if n == 0:
            return 1.0
        if n % 2 == 0:
            return self.pow(x * x, n / 2)
        else:
            return x * self.pow(x * x, n / 2)
