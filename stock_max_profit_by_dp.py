#-*- coding:utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-26
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type prices: List[int]
        :rtype: int
        """
        
        #获取股票交易天数，用于后续代码复用
        num_of_stock_trade_days = len(prices)
        
        #如果仅有1天交易时间，就无法完成买卖交易，则0利润
        if num_of_stock_trade_days == 0:
            return 0
        
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #第1天，无卖出操作，所以利润为0：f[0] = 0
        #最小价格记录（当天之前范围内）
        lowest_price = prices[0]
        #定义当天最大利润数组，用于存储当天最大利润值，初始化为0
        max_profit = [0] * num_of_stock_trade_days
        
        #归纳递推（状态转移方程）
        #第i天时：f(i) = prices[i] - min(prices[j] ), j∈0~i-1
        for i in range(1, num_of_stock_trade_days):
            #从最低点入手，最高点卖出，低点需要再卖出点之前
            max_profit[i] = max(max_profit[i], prices[i] - lowest_price)
            #通过持续比较，记录最低价格，用于最大利润计算
            lowest_price = min(prices[i], lowest_price)
            
        #最终加一条，求取所有交易值的最大值即可: max_profit = max(f(i)),i ∈0~len(prices)
        return max(max_profit)
        
if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    prices = [7,1,5,3,6,4]
    # 输出：5
    # 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
    #     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
    print('示例1：', cs.maxProfit(prices))
    
    # 示例 2
    # 输入
    prices = [7,6,4,3,1]
    # 输出：0
    # 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
    print('示例2：', cs.maxProfit(prices))