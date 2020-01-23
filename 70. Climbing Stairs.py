class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        return self.getCount(0, n)

    def getCount(self, current, n):
        if current > n:
            return 0
        if current == n:
            return 1
        if current in self.cache: return self.cache[current]

        result = (self.getCount(current + 1, n) + self.getCount(current + 2, n))
        self.cache[current] = result

        return result

