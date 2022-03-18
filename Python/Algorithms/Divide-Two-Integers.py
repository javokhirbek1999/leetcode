class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = int(dividend/divisor)
        if q > pow(2, 31)-1:
            return pow(2, 31)-1
        elif q < -pow(2, 31):
            return -pow(2, 31)
        else:
            return q
