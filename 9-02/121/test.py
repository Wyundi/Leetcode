prices = [7,1,5,3,6,4]

def maxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]

    for i in range(len(prices)):
        minPrice = min(prices[i], minPrice)
        maxProfit = max((prices[i] - minPrice), maxProfit)     

    return maxProfit

print(maxProfit(prices))