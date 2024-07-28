#-*- coding:utf-8 -*-

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        
        #Author: ShanGouXuehui
        #Date: 2024-7-28
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        import math
        
        #定义dp数组，用于存储数组，默认输掉比赛；状态转移方程中，只需计算赢游戏的逻辑即可
        if_win_flag = [False] * (n + 1)
        
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #当没有石子，先手的取不到石子，记为输掉游戏：f[0] = False
        if_win_flag[0] = False
        
        #归纳递推（状态转移方程）
        #第i个石堆时：f[i] =  True  if  f[i - j^2] == False
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                #第i个石堆时：f[i] =  True  if  f[i - j^2] == False
                if not if_win_flag[i - j*j]:
                    if_win_flag[i] = True
                    #两个人都采取最优策略,赢了就停止计算
                    break
                
        # print(if_win_flag)
                
        return if_win_flag[n]
     

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入：
    n = 1
    # 输出：true
    # 解释：Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。
    print('示例1：', cs.winnerSquareGame(n))
    print('------------------------------------------------------')
    
    # 示例 2
    # 输入：
    n = 2
    # 输出：false
    #解释：Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -> 1 -> 0）。
    print('示例2：', cs.winnerSquareGame(n))
    print('------------------------------------------------------')
    
    # 示例 3
    # 输入：
    n = 4
    # 输出：true
    # 解释：n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -> 0）。
    print('示例3：', cs.winnerSquareGame(n))
    print('------------------------------------------------------')
    
    # 示例 4
    # 输入：
    n = 7
    # 输出：false
    # 解释：当 Bob 采取最优策略时，Alice 无法赢得比赛。
    # 如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 3 -> 2 -> 1 -> 0）。
    # 如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 6 -> 2 -> 1 -> 0）。
    print('示例4：', cs.winnerSquareGame(n))