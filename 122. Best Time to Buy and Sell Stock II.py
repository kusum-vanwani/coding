class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        a = prices[0]
        current_max = float('-inf')
        profit = 0

        i = 1
        while i < len(prices):
            prof = prices[i] - a
            if prof < 0:
                a = prices[i]
                if current_max != float('-inf'):
                    profit = profit + current_max
                    current_max = float('-inf')
            if prof >= 0 and prof > current_max:
                current_max = prof
            elif prof >= 0 and prof < current_max:
                profit = profit + current_max
                current_max = float('-inf')
                a = prices[i]

            i = i + 1
        if current_max != float('-inf'):
            profit = profit + current_max
        return profit


s = Solution()
num = [7,1,5,3,6,4]
print s.maxProfit(num)