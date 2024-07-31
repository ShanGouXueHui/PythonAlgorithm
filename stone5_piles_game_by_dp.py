#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        
        #超时
        
        
        #Author: ShanGouXuehui
        #Date: 2024-7-30
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        num_of_stones = len(stoneValue)
        
        #计算累计值
        accumulate_value = [0 for _ in range(num_of_stones)]
        
        accumulate_value[0] = stoneValue[0]        
        for index in range(1, num_of_stones):
            accumulate_value[index] = accumulate_value[index-1] + stoneValue[index]
        
        #定义dp数组，用于存储最大值；最后一个石子得分为0，所以可以通过倒序来求最大值
        #max_stone_value[i][j] 表示合并区间 i ~ j 所能获得的最大收益
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #当只有1颗石子的时候，游戏结束，分数为0：f[i] [i] = stoneValue[i]
        max_stone_value = [[0] * num_of_stones for _ in range(num_of_stones)]
                
        #先枚举区间长度
        for l in range(2, num_of_stones + 1):
            #再枚举起点
            for left_index in range(num_of_stones):
                #计算终点
                right_index = left_index + l - 1 
                
                #如果超出范围则停止计算
                if right_index >= num_of_stones:
                    break
                
                #遍历中间选点，计算所有值
                for i in range(left_index, right_index): 
                    if left_index == 0:
                        left_sum = accumulate_value[i]
                    else:
                        left_sum = accumulate_value[i] - accumulate_value[left_index - 1]
                    right_sum = accumulate_value[right_index] - accumulate_value[i]
                    
                    
                    #状态转移方程1：如果sum(stoneValue [left_index: i + 1]) > sum(stoneValue [i + 1: right_index+1]) ，
                    # 那么Bob会丢弃左侧部分，状态转移方程为f[left_index][right_index] = f[i+1][right_index]+ sum(stoneValue [i + 1: right_index+1]) 
                    if left_sum > right_sum:
                        max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index],max_stone_value[i+1][right_index]+ right_sum)
                    #状态转移方程2：如果sum(stoneValue [left_index: i + 1]) < sum(stoneValue [i + 1: right_index+1]) ，
                    # 那么Bob会丢弃右侧部分，状态转移方程为f[left_index][right_index] = f[left_index][i] + sum(stoneValue [left_index: i + 1]) 
                    elif left_sum < right_sum:
                        max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index], max_stone_value[left_index][i] + left_sum)
                    #状态转移方程3：如果sum(stoneValue [left_index: i + 1]) == sum(stoneValue [i + 1: right_index])，那么Alice选择一个最有利的选项。
                    # f[left_index][right_index] = max(f[left_index][i], f[i+1][right_index])+ sum(stoneValue [left_index: i + 1]) 
                    else:
                        max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index], max(max_stone_value[i+1][right_index]+ right_sum, max_stone_value[left_index][i] + left_sum))
                    
        #最终返回最长的完整线段的最大得分
        return max_stone_value[0][num_of_stones-1]   

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    stoneValue = [6,2,3,4,5,5]
    # 输出：18
    # 解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
    # 在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
    # 最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。
    print('示例1：', cs.stoneGameV(stoneValue))
    
    # 示例 2：
    # 输入：
    stoneValue = [7,7,7,7,7,7,7]
    # 输出：28
    print('示例2：', cs.stoneGameV(stoneValue))
    
    # 示例 3：
    # 输入：
    stoneValue = [4]
    # 输出：0
    print('示例3：', cs.stoneGameV(stoneValue))
    
    # 示例 4：
    # 输入：
    stoneValue = [9,8,2,4,6,3,5,1,7]
    # 输出：34
    print('示例4：', cs.stoneGameV(stoneValue))