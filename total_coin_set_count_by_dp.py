#-*- coding:utf-8 -*-

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-7-14
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
               
        #如果amount为0，返回1
        #当总金额为0时，组合数是1（0个硬币）：f(0) = 1
        if amount == 0:
            return 1
        
        #定义dp数组，用于存储硬币组合个数, 由于是求和，默认为0
        total_num_of_coin_set = [0] * (amount + 1)
        total_num_of_coin_set[0] = 1
        
        #这里需要处理一种特殊情况：a + b = b + a, 也就是说可能会出现顺序不同的重复组合。
        #在遍历的时候，先遍历硬币，再遍历总额；这样硬币访问就有了顺序，总是a + b。
        for coin in coins:
            ##当总金额小于硬币面值是，组合数是0（无法给出相应组合）：f(i) = 0, i < coins[j]
            #所以起始值直接是coin
            for i in range(coin, amount + 1):                 
                #假设，coins[j]是组合的最后一个硬币，那么组合数有f(i- coins[j]), 
                # 那么所有的组合数f(i) = sum(f(i- coins[j]), j ∈ 0~len(coins[j])。
                #所以组合总数，是针对每个硬币面值求和
                total_num_of_coin_set[i] += total_num_of_coin_set[i - coin] 
        #返回最终值
        return total_num_of_coin_set[amount]
        
        

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    amount = 5
    coins = [1, 2, 5]
    # 输出：4
    # 解释：有四种方式可以凑成总金额：
    print('示例1：', cs.change(amount,coins))
    
    # 示例 2
    # 输入
    amount = 3
    coins = [2]
    # 输出：0
    #只用面额 2 的硬币不能凑成总金额 3 。
    print('示例2：', cs.change(amount,coins))
        
    # 示例 3
    # 输入
    amount = 10
    coins = [10] 
    # 输出：1
    print('示例3：', cs.change(amount,coins))
    
    