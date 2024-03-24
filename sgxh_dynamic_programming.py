#-*- coding:utf-8 -*-

# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 

# 示例 1：
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

# 提示：
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

def dp_stock_k_trades(K:int, prices:list[int]):
    prices_length = len(prices)
    #至少2天才能完成一次交易，所以小于2天的直接返回利润为0
    if prices_length < 2:
        return 0
    
    #由于同时只能进行一次交易，所以最多进行prices_length/2次交易。
    #如果大于这个数，就算是不限次数了,所以就不用单独考虑交易次数了
    if K >= prices_length/2:
        #定义dp table，避免重复计算, 1维是天数，2维代表是否存持有股票（0 - 未持， 1 - 持有）
        #初始化为0
        dp_max_profit = [[0 for j in range(2)] for g in range(prices_length)]
        #初始化第一天的值，作为基线值
        #如果未持有股票，则没有发生买卖，则利润为0
        dp_max_profit[0][0] = 0
        #如果持有股票，则值为购买股票的负值
        dp_max_profit[0][1] = -prices[0]
        
        #利用状态（天数、交易、是否持有股票），生成状态转移方程，计算最大利润
        #用白话描述最大利润，就是将每次能挣钱的股票采购，都要完成，然后加起来即可（贪心算法也可以完成）
        for i in range(1, prices_length):
            #当天没有持有股票，有两种可能：
            #1、昨天就没有持有，今天还是没有持有，无变化；
            #2、昨天持有股票，今天卖掉昨天的股票，获取收入，同时今天没有持有股票。
            dp_max_profit[i][0] = max(dp_max_profit[i-1][0], dp_max_profit[i-1][1] + prices[i])
            # 当天持有着股票，有两种可能：
            # 1、昨天就持有着股票，今天还持有着股票，无变化；
            # 2、昨天本没有持有，今天我持有股票，就要付出金额购买股票，同时今天持有股票。
            # 3、允许的最大交易次数减少了一次，因为每次买入操作会使用一次交易。
            dp_max_profit[i][1] = max(dp_max_profit[i-1][1], dp_max_profit[i-1][0] - prices[i])
        
        #为什么选择dp_max_profit[prices_length - 1][0] 为最终结果：因为 [1] 代表⼿上还持有股票，
        #[0] 表⽰⼿上的股票已经卖出去了，显然后者得到的利润⼀定⼤于前者。
        print('打印dp table，印证算法：',dp_max_profit)
        print('最大利润：',dp_max_profit[prices_length - 1][0] )
        return dp_max_profit[prices_length - 1][0] 
    
    #对于有限的交易次数，则始终保持K次交易获取到了最大利润，方便累计相加求取最大利润值
    else:
        #定义dp table，避免重复计算, 1维是天数，2维代表交易次数，3维代表是否存持有股票（0 - 未持， 1 - 持有）
        #初始化为0
        dp_max_profit = [[[0 for j in range(2)] for k in range(K + 1)] for g in range(prices_length)]
        #初始化第一天的值，作为基线值
        for k in range(K + 1):
            #如果未持有股票，则没有发生买卖，无论是第几次交易，则利润为0
            dp_max_profit[0][k][0] = 0
            #如果持有股票且是第一次购买股票，无论是第几次交易，则值为购买股票的负值
            dp_max_profit[0][k][1] = -prices[0]
        
        #利用状态（天数、交易、是否持有股票），生成状态转移方程，计算最大利润
        #用白话描述最大利润，就是将Top K次挣钱最多的股票采购，加起来即可
        for i in range(1, prices_length):
            for k in range(1, K + 1):
                #当天没有持有股票，有两种可能：
                #1、昨天就没有持有，今天还是没有持有，无变化；
                #2、昨天持有股票，今天卖掉昨天的股票，获取收入，同时今天没有持有股票。
                dp_max_profit[i][k][0] = max(dp_max_profit[i-1][k][0], dp_max_profit[i-1][k][1] + prices[i])
                # 当天持有着股票，有两种可能：
                # 1、昨天就持有着股票，今天还持有着股票，无变化；
                # 2、昨天本没有持有，今天我持有股票，就要付出金额购买股票，同时今天持有股票。
                # 3、允许的最大交易次数减少了一次，因为每次买入操作会使用一次交易。
                dp_max_profit[i][k][1] = max(dp_max_profit[i-1][k][1], dp_max_profit[i-1][k - 1][0] - prices[i])
        
        #为什么选择dp_max_profit[prices_length - 1][0] 为最终结果：因为 [1] 代表⼿上还持有股票，
        #[0] 表⽰⼿上的股票已经卖出去了，显然后者得到的利润⼀定⼤于前者。
        print('打印dp table，印证算法：',dp_max_profit)
        print('最大利润：',dp_max_profit[prices_length - 1][K][0] )
        return dp_max_profit[prices_length - 1][K][0] 



if __name__ == '__main__':
    #实例1
    k = 1
    prices = [7,1,5,3,6,4]
    #输出5
    dp_stock_k_trades(k, prices)
    
    #实例2
    k = 1
    prices = [7,6,4,3,1]
    #输出0
    dp_stock_k_trades(k, prices)
    
    #实例3
    k = 2
    prices = [2,4,1]
    #输出2
    dp_stock_k_trades(k, prices)
    
    #实例3
    k = 2
    prices = [3,2,6,5,0,3]
    #输出7
    dp_stock_k_trades(k, prices)
    
    #实例4
    k = 2
    prices = [3,3,5,0,0,3,1,4]
    #输出6
    dp_stock_k_trades(k, prices)