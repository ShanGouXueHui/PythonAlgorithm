#-*- coding:utf-8 -*-

class Solution(object):
    def maxProfit(self, k, prices):
        """
        #Author: ShanGouXuehui
        #Date: 2024-7-5
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        #交易天数，用于后续代码复用
        num_of_trade_days = len(prices) 
        
        #由于，不能并行进行多次交易，那么最多进行num_of_trade_days//2次交易 - 一天买，一天卖
        #重新定义一下交易次数k
        k = min(k, num_of_trade_days//2)
        
        #定义dp数组，存储累计的利润:f[i][j][0 or 1], 倒序定义
        #赋值dp的时候，顺序相反，最里面是是否持有股票，中间是第几次交易，最后是交易天数
        #从没有交易开始，第0天开始，用于设置初始值
        accumulate_profit = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(num_of_trade_days+1)]
        
        #归纳奠基，初始数据
        #针对第0天
        for j in range(k+1):
            #未持有股票状态：交易还没有开始，这时候的利润是 0
            accumulate_profit[0][j][0] = 0
            #持有股票状态：交易没有开始是不可能持有股票的，⽤负⽆穷表⽰这种不可能（求得是最大利润，所以只要产生交易，此值就会被舍弃）
            accumulate_profit[0][j][1] = float('-inf')
        #针对第0次交易
        for i in range(num_of_trade_days+1):
            #未持有股票状态：根本不允许交易，这时候利润当然是 0
            accumulate_profit[i][0][0] = 0
            #持有股票状态：不可能持有股票，用负无穷表示不可能（求得是最大利润，所以只要产生交易，此值就会被舍弃）
            accumulate_profit[i][0][1] = float('-inf')
                
        #2)归纳递推（状态转移方程）
        # 第i天时：
        # f[i][j][0]= max(f[i-1][j][0], f[i-1][j][1] + prices[i])
        # f[i][j][1]= max(f[i-1][j][1], f[i-1][j-1][0] - prices[i])        
        for i in range(1, num_of_trade_days+1):
            for j in range(1, k + 1):
                accumulate_profit[i][j][0]= max(accumulate_profit[i-1][j][0], accumulate_profit[i-1][j][1] + prices[i-1])  
                accumulate_profit[i][j][1]= max(accumulate_profit[i-1][j][1], accumulate_profit[i-1][j-1][0] - prices[i-1])
         
        #3)最后加一条，最大利润是f[n−1][k-1][0] 
        return accumulate_profit[num_of_trade_days][k][0]
       
        

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    k = 2
    prices = [2,4,1]
    # 输出：2
    # 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    print('示例1：', cs.maxProfit(k, prices))
    
    
    # 示例 2
    # 输入
    k = 2
    prices = [3,2,6,5,0,3]
    # 输出：7
    # 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
    #  随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
    print('示例2：', cs.maxProfit(k, prices))