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
        
        #获取交易天数，用于后续代码复用
        num_of_trade_days = len(prices)
        
        #如果仅有一天，那么交易无异议，返回0
        if num_of_trade_days == 1:
            return 0
        
        #定义dp数组，用于存储累加的利润值; 第1维代表交易的天数，第2维代表第几次交易，第3维代表是否持有股票
        #定义股票的时候，顺序相反，最里面是是否持有股票，中间是第几次交易，最后是交易天数
        accumulate_profit = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(num_of_trade_days)]
        
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        # 第1天利润：f[0][0][0] = 0, f[0][0][1] = -prices[0], f[0][1][0] = 0, f[0][1][1] = -prices[0],
        accumulate_profit[0][0][0] = 0
        accumulate_profit[0][0][1] = -prices[0]
        accumulate_profit[0][1][0] = 0
        accumulate_profit[0][1][1] = -prices[0]
        
        #归纳递推（状态转移方程）
        # 第i天时：
        # f[i][0][0]= max(f[i-1][0][0], f[i-1][0][1] + prices[i]);
        # f[i][1][0]= max(f[i-1][1][0], f[i-1][1][1] + prices[i]);
        # f[i][0][1] = max(f[i-1][0][1],f[i-1][0][0] - prices[i]);
        # f[i][1][1] = max(f[i-1][1][1],f[i-1][0][0] - prices[i])
        for i in range(1, num_of_trade_days):
            #首先，看一下没有持有股票的情况f[i][0][0]和f[i][1][0]如果第i天没有持有股票，那么如下可能情况：            
            # 第一次交易：f[i][0][0]
            # 一是第i-1天也没有持有股票，那么当天收益和昨天一样f[i][0][0] = f[i-1][0][0]。
            # 另外一种情况是，第i-1天有股票，在第i天卖掉，卖掉相当于有了收入f[i][0][0]  = f[i-1][0][1] + prices[i]。
            # 我们求的是最大利润，所以最终：f[i][0][0]= max(f[i-1][0][0], f[i-1][0][1] + prices[i])
            accumulate_profit[i][0][0]= max(accumulate_profit[i-1][0][0], accumulate_profit[i-1][0][1] + prices[i])
            # 第二次交易：f[i][1][0]
            # 一是第i-1天也持有股票，那么当天收益和昨天一样f[i][1][0] = f[i-1][1][0]。
            # 另外一种情况是，第i-1天有股票，在第i天卖掉，卖掉相当于基于第2次购入股票的基础上，
            # 有了收入f[i][1][0]  = f[i-1][1][1] + prices[i]。
            # 我们求的是最大利润，所以最终：f[i][1][0]= max(f[i-1][1][0], f[i-1][1][1] + prices[i])
            accumulate_profit[i][1][0]= max(accumulate_profit[i-1][1][0], accumulate_profit[i-1][1][1] + prices[i])
            
            #然后，看一下持有股票的情况f[i][0][1]和f[i][1][1]
            # 第一次交易：f[i][0][1]
            # 一是第i-1天也持有，那么当天收益和昨天一样f[i][0][1] = f[i-1][0][1]。
            # 另外一种情况是，第i-1天没股票，在第i天买入的，买入就要花钱，那么f[i][0][1] = - prices[i]。
            # 同样，我们求得是最大利润，所以最终：f[i][0][1] = max(f[i-1][0][1], - prices[i])
            accumulate_profit[i][0][1]= max(accumulate_profit[i-1][0][1], - prices[i])
            
            #第二次交易：f[i][1][1]
            # 一是第i-1天也持有，那么当天收益和昨天一样 f[i][1][1] = f[i-1][1][1]。
            # 另外一种情况是，第i-1天没股票，在第i天买入的，买入就要花钱，相当于基于第1次交易的利润的基础上，
            # 采购股票，那么f[i][1][1] = f[i-1][1][0] - prices[i]。
            # 同样，我们求得是最大利润，所以最终：f[i][1][1] = max(f[i-1][1][1],f[i-1][1][0] - prices[i])
            accumulate_profit[i][1][1]= max(accumulate_profit[i-1][1][1], accumulate_profit[i-1][0][0] - prices[i])
        
        #最后，全部n次交易结束后的结果
        #持有股票（买入花钱）的收益一定低于不持有股票（卖出收钱）的收益，同时第二笔交易累计利润肯定大于第一笔，所以最大利润是f[n−1][1][0]。
        return accumulate_profit[num_of_trade_days-1][1][0]
        
        
        
if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    prices = [3,3,5,0,0,3,1,4]
    # 输出：6
    # 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    #  随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 
    print('示例1：', cs.maxProfit(prices))
    
    # 示例 2
    # 输入
    prices = [1,2,3,4,5]
    # 输出：4
    # 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
    #  注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
    #  因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    print('示例2：', cs.maxProfit(prices))
    
    # 示例 3
    # 输入
    prices = [7,6,4,3,1] 
    # 输出：0
    # 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
    print('示例3：', cs.maxProfit(prices))