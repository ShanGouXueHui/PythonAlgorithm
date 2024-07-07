#-*- coding:utf-8 -*-

class Solution(object):
    def maxProfit(self, prices, fee):
        """        
        #Author: ShanGouXuehui
        #Date: 2024-7-7
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type prices: List[int]
        :type fee: int
        :rtype: int      
        """
        #获取交易天数，用于后续代码复用
        num_of_trade_days = len(prices)
        
        #如果仅有一天，那么交易无异议，返回0
        if num_of_trade_days == 1:
            return 0
        
        #定义dp数组，用于存储累加的利润值
        accumulate_profit = [[0]*2]*num_of_trade_days
        
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #第1天利润：f[0][0] = 0, f[0][1] = -prices[0]
        accumulate_profit[0][0] = 0
        accumulate_profit[0][1] = -prices[0]
        
        #归纳递推（状态转移方程）
        #第i天时：f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i] - fee)；
        #f[i][1] = max(f[i-1][1],f[i-1][0] - prices[i])
        for i in range(1, num_of_trade_days):
            #如果第i天没有持有股票，那么有可能情况：一是第i-1天也没有，那么当天收益和昨天一样f[i][0] = f[i-1][0]；
            #另外一种情况是，第i-1天有股票，在第i天卖掉，卖掉相当于有了收入f[i][0] = f[i-1][1] + prices[i]。
            accumulate_profit[i][0] = max(accumulate_profit[i-1][0], accumulate_profit[i-1][1] + prices[i] - fee)
            #如果第i天持有股票，那么有两种情况：一是第i-1天也持有，那么当天收益和昨天一样f[i][1] = f[i-1][1]；
            #另外一种情况是，第i-1天没股票，在第i天买入的，买入就要花钱
            accumulate_profit[i][1] = max(accumulate_profit[i-1][1],accumulate_profit[i-1][0] - prices[i])
        
        #持有股票（买入花钱）的收益一定低于不持有股票（卖出收钱）的收益f[n−1][0] 收益必然是大于f[n−1][1] 的，
        #所以最大利润是f[n−1][0] 。
        return accumulate_profit[num_of_trade_days-1][0]
        

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    # 输出：8
    # 解释：能够达到的最大利润:  
    # 在此处买入 prices[0] = 1
    # 在此处卖出 prices[3] = 8
    # 在此处买入 prices[4] = 4
    # 在此处卖出 prices[5] = 9
    # 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
    print('示例1：', cs.maxProfit(prices, fee))
    
    # 示例 2
    # 输入
    prices = [1,3,7,5,10,3]
    fee = 3
    # 输出：6
    print('示例2：', cs.maxProfit(prices, fee))