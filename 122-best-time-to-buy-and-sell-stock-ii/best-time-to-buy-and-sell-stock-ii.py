class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy=prices[0]
        # sell=0
        # buyind=0
        # sellind = 0
        # total = 0
        # k=0
        # pricelen=len(prices)
        # while k < pricelen:
        #     print("initial",prices)
        #     for i in prices:
        #         if i < buy:
        #             buy = i
        #             buyind=prices.index(i)
        #             print("buy",buy)
        #             break
        #     print(prices[buyind:])
        #     for j in prices[buyind:]:
        #         if j > buy:
        #             sell = j
        #             sellind=prices.index(j)
        #             print("sell",sell)
        #             break
        #         else:
        #             sell = buy

        #     print(buy,sell)
        #     if (sell - buy )!=0:
        #         total = total + (sell - buy)
        #     else:
        #         total = total
        #     print("total",total)
        #     if sellind < pricelen:
        #         prices=prices[sellind+1:]
        #     else:
        #         return total
        #     k=k+1
        #     print("last",prices)
        #     if len(prices) != 0: 
        #         print("sas",prices[0])
        #         buy=prices[0]
        #         sell=0
        #         buyind=0
        #         sellind = 0
        # return total


        max = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max