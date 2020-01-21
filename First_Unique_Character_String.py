class Solution:
    def firstUniqChar(self, s) :
        collection = {}
        for i, v in enumerate(s):
            if v in collection:
                collection[v] = -1
            else:
                collection[v] = i

        mini = float('inf')
        for ib in collection.values():
            if ib != -1 and ib < mini:
                mini = ib
        if mini == float('inf'):
            return -1
        else:
            return mini


s = Solution()
st = "loveleetcode"
s.firstUniqChar(st)
print(s.firstUniqChar(st))