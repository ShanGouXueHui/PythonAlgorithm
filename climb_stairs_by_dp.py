#-*- coding:utf-8 -*-

#Author: ShanGouXuehui
#Date: 2024-5-29
#Git: https://github.com/ShanGouXueHui/PythonAlgorithm
#Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
#Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #爬楼梯的方法总数，是斐波那契数列f(n) = f(n-1) + f(n-2)，详细分析可以看原文分析
        #本算法按照动态规划算法实现
        
        #如果只有1阶或者2阶，则直接返回结果
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        #定义dp数组，存储重叠子问题的值, 索引从0开始，所以构建dp的时候多+1个位置
        climb_methods = [0 for _ in range(n+1)]
        #首先初始化第1个值（第1个阶梯）和第2个值（第2个阶梯）
        climb_methods[1] = 1
        climb_methods[2] = 2
        
        #最终结果存储
        result = 0
        #递推n阶阶梯是，有多少种爬楼梯的方法
        #从第3阶开始，值第n阶
        for stair in range(3, n+1):
            climb_methods[stair] = climb_methods[stair - 1] + climb_methods[stair - 2] 
        
        return climb_methods[n]
         
        
if __name__ == "__main__":
    cs = Solution()
    
    #示例 1
    #输入：
    n = 2
    #输出：2
    # 解释：有两种方法可以爬到楼顶。
    # 1. 1 阶 + 1 阶
    # 2. 2 阶
    print(cs.climbStairs(n))
    
    #示例2
    #输入
    n = 3
    # 输出：3
    # 解释：有三种方法可以爬到楼顶。
    # 1. 1 阶 + 1 阶 + 1 阶
    # 2. 1 阶 + 2 阶
    # 3. 2 阶 + 1 阶
    print(cs.climbStairs(n))