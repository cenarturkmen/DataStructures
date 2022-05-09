
#  o(n^2) time
def buyAndSellStockOnce(arr):
    profit = 0
    maxProfit = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)-1):
            profit = arr[j] - arr[i]
            maxProfit = max(maxProfit, profit)

    return maxProfit

print(buyAndSellStockOnce([310,315,275,295,260,270,290,230,255,250])) 

#  o(n) time
def buyAndSellStockOnce2(arr):
    profit = 0
    maxProfit = 0
    minPriceSoFar = float('inf')

    for  i in range(len(arr)-1):
        profit = arr[i] - minPriceSoFar
        maxProfit = max(maxProfit, profit)
        minPriceSoFar = min(minPriceSoFar, arr[i])
    
    return maxProfit

print(buyAndSellStockOnce2([310,315,275,295,260,270,290,230,255,250]))