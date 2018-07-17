class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            return b if a % b == 0 else gcd(b, a % b)
        
        if z == 0: return True
        elif x == 0 or y == 0 or (z > x + y): return False
        return not bool(z % gcd(x, y))