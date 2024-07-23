#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        
        #Author: ShanGouXuehui
        #Date: 2024-7-23
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获取石子堆数，用于后续的代码复用        
        num_of_piles = len(stoneValue)
        #存储为当前剩下的石子堆的总石子数目
        total_left_stone_count = 0
                
        #定义dp数组，存储当前玩家能拿到的最大石子数目
        #在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子, 超出石子堆范围的获取值为0
        #为了方便计算，我们将dp数组长度增加3个位
        max_stone_dp = [0 for _ in range(num_of_piles + 3)]
        
        #当石子堆就剩1堆的时候，玩家可以全部取走；这个用例可以作为基础用例
        max_stone_dp[num_of_piles - 1] = stoneValue[-1]
        
        #两个玩家获取石子的关系：第一个玩家的石子数 = 总石子数 - 第二个玩家的石子数
        #使用倒序方式来表达状态转移方程,f[i] = total_num_of_rest_stone  - min(f[j]), j 属于 [i + 1,i + 3]
        for i in range(num_of_piles - 1, -1, -1):
              total_left_stone_count += stoneValue[i]
              max_stone_dp[i] = total_left_stone_count  - min(max_stone_dp[i+1:i+4])
              
        total_stone_count = sum(stoneValue)
        
        #如果两个玩家获取的石子相等，则返回Tie
        if max_stone_dp[0] * 2 == total_stone_count:
            return 'Tie'
        elif max_stone_dp[0] * 2 > total_stone_count:
            return 'Alice'
        else:
            return 'Bob'         

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    values = [1,2,3,7]
    # 输出："Bob"
    #Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
    print('示例1：', cs.stoneGameIII(values))
    
    # 示例 2
    # 输入
    values = [1,2,3,-9]
    # 输出："Alice"
    print('示例2：', cs.stoneGameIII(values))
    
    # 示例 3
    # 输入
    values = [1,2,3,6]
    # 输出："Tie"
    print('示例3：', cs.stoneGameIII(values))