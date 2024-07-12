#-*- coding:utf-8 -*-


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-7-13
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获取硬币面值数量，用于后续代码复用
        num_of_coins = len(coins)
        
        #如果amount为0，返回0
        if amount == 0:
            return 0
        
        #定义dp数组，用于存储最小硬币个数, 默认无穷大，方便求最小值
        min_num_of_coins = [float('inf') for _ in range(amount + 1)]
   
        #归纳递推（状态转移方程）
        #第i天时：f(i) = min(f(i - coin[j]) + 1) j ∈ len（coin）
        for i in range(1, amount + 1):
            for coin in coins:
                #至少要有1个硬币才有意义，所以从硬币的面值开始
                if i < coin or coin > (amount + 1):
                    continue
                # 归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
                #当达到打到1枚硬币面值的总金额时，数量是1
                if i == coin:
                    min_num_of_coins[coin] = 1
                #归纳递推（状态转移方程）
                #第i天时：f(i) = min(f(i - coin[j]) + 1) j ∈ len（coin）
                min_num_of_coins[i] = min(min_num_of_coins[i], min_num_of_coins[i - coin] + 1)
                
        #最终，如果没有任何一种硬币组合能组成总金额，返回 -1 
        return min_num_of_coins[amount] if min_num_of_coins[amount] != float('inf') else -1
        
        
if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    coins = [1, 2, 5]
    amount = 11
    # 输出：3
    # 解释：11 = 5 + 5 + 1。
    print('示例1：', cs.coinChange(coins,amount))
    
    # 示例 2
    # 输入
    coins = [2]
    amount = 3
    # 输出：-1
    print('示例2：', cs.coinChange(coins,amount))
    
    # 示例 3
    # 输入
    coins = [1]
    amount = 0
    # 输出：0
    print('示例3：', cs.coinChange(coins,amount))
    
    # 示例 4
    # 输入
    coins = [2]
    amount = 1
    # 输出：-1
    print('示例3：', cs.coinChange(coins,amount))