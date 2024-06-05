#-*- coding:utf-8 -*-

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-05
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type cost: List[int]
        :rtype: int
        """
        #获取阶梯数
        no_of_stairs = len(cost)
        #定义dp数组，存储过程值，避免重复计算        
        #全部费用初始化为0
        least_cost_list = [0] * (no_of_stairs + 1)
        
        #根据状态转移方程，求取到达n阶时最小费用：f(n) = min(f(n-1) + cost[n-1]，f(n-2) + cost[n-2])
        #由于到达第0个阶梯和第1个阶梯，没有前置费用，所以 f(0) = cost[0]; 阶梯为1时：f(1) = cost[1]。
        #所以计算值可以直接从第2阶开始
        for i in range(2, no_of_stairs + 1):
            least_cost_list[i] = min(least_cost_list[i-1] + cost[i-1], least_cost_list[i-2] + cost[i-2])
        
        #返回顶部所需最小费用
        return least_cost_list[no_of_stairs]
        



if __name__ == "__main__":
    cs = Solution()
    
    #示例 1
    #输入：
    cost = [10,15,20]
    #输出：15
    # 解释：将从下标为 1 的台阶开始。
    # - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
    # 总花费为 15 。
    print('示例1：', cs.minCostClimbingStairs(cost))
    
    #示例 2
    #输入：
    cost = [1,100,1,1,1,100,1,1,100,1]
    # 输出：6
    # 解释：你将从下标为 0 的台阶开始。
    # - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
    # - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
    # - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
    # - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
    # - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
    # - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
    # 总花费为 6 。
    print('示例2：', cs.minCostClimbingStairs(cost))