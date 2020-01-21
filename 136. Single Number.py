class Solution:
    def singleNumber(self, nums):
        collection = set()

        for i in nums:
            if i in collection:
                collection.remove(i)
            else:
                collection.add(i)

        for j in collection:
            return j

        return -1

s = Solution()
st = [4,1,2,1,2]
s.singleNumber(st)
print(s.singleNumber(st))