#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-7-22
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获取石子堆数，用于后续的代码复用        
        num_of_piles = len(piles)
        #存储为当前剩下的石子堆的总石子数目
        total_left_stone_count = 0
        
        #如果只有一堆石子，则直接返回结果
        if num_of_piles == 1:
            return piles[0]
        
        #定义dp方程
        # max_stone_dp[i][j] 代表当剩下的石子堆为 piles[i…n−1] 且 M=j 时当前玩家能拿到的最大石子数目
        max_stone_dp = [[0 for _ in range(num_of_piles)] for _ in range(num_of_piles)]
        
        #因为当玩家可以取的堆数2M, 大于剩余石子堆数，可以直接取走所有石子，这个值可以确定作为初始值，
        # 所以循环采用倒序方式。
        for i in range(num_of_piles - 1, -1, -1):
              total_left_stone_count += piles[i]
              #当 M=j时，当前玩家可以选择从最左边开始拿走m堆石子，其中 1≤m≤2M
              #因此能获得的最大石子数目 = total_left_stone_count - 另一个人按照最优策略能拿到的最大石子数目
              for j in range(1, num_of_piles):
                  #初始条件：当玩家可以取的堆数2M, 大于剩余石子堆数，可以直接取走所有石子
                  #第i堆石子，也可以取走
                  if 2*j >= num_of_piles - i:
                      max_stone_dp[i][j] = total_left_stone_count
                      continue
                  #状态转移方程： 玩家能获得的最大石子数目 = 剩余石子数量 - 另外一人取得的最大石子数量
                  for m in range(1, 2*j + 1):
                      max_stone_dp[i][j] = max(max_stone_dp[i][j], total_left_stone_count - max_stone_dp[i+m][max(m,j)])
        #M从1开始，所以取值max_stone_dp[0][1]  
        return max_stone_dp[0][1]                           
                    
            
       
        

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    piles = [2,7,9,4,4]
    # 输出：10
    #如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，
    # 那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
    print('示例1：', cs.stoneGame(piles))
    
    # 示例 2
    # 输入
    piles = [1,2,3,4,5,100]
    # 输出：104
    print('示例2：', cs.stoneGame(piles))
    
    # 示例 3
    # 输入
    piles = [1]
    # 输出：1
    print('示例3：', cs.stoneGame(piles))