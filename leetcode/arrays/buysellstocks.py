#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# o(n) time o(1) space complexity
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        compare = price - min_price
        max_profit = max(max_profit, compare)


    return max_profit


#o(n^2) time o(1) space complexity
def maxProfit(p):
        n = len(p)
        max_so_far = 0

        for i in range(n):
            for j in range(i+1,n):
                max_so_far = max(max_so_far, p[j] - p[i])

        return max_so_far


# sliding window solution o(n) time - o(1) space complexity
def maxProfit3(prices):
        
    left = 0 
    right = 0
    maxprofit = 0
        
    while right < len(prices):
        maxprofit = max(maxprofit, prices[right] - prices[left])
        if (prices[left] > prices[right]):
            left +=1
        else:
            right += 1
            
    return maxprofit