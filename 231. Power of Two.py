class Solution:
    def isPowerOfTwo(self, n) :
        while n > 1:
            n = n / 2

        if n != 1:
            return False
        else:
            return True

s = Solution()
num = 1024
print(s.isPowerOfTwo(num))