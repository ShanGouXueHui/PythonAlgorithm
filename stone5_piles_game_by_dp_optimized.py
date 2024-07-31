#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-7-31
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获取值的最大长度，用于后续的复用
        num_of_stones = len(stoneValue)
        
        #存储alice存储的最大分支
        max_stone_value = [[0] * num_of_stones for _ in range(num_of_stones)]
        #存储左边最大值，和右边最大值，避免重复计算
        left_max_value = [[0] * num_of_stones for _ in range(num_of_stones)]
        right_max_value = [[0] * num_of_stones for _ in range(num_of_stones)]
        
        #状态转移方程：Bob会丢弃值最大的行，Alice的得分为剩下那行的值（每轮累加）。
        # 如果两行的值相等，Bob让Alice决定丢弃哪一行（保留收益大的哪一行）
        for left_index in range(num_of_stones - 1, -1, -1):
            #当前石子为分割石时，左右最大可以的分值，就是该石子对应的分值
            #用于基础值计算
            left_max_value[left_index][left_index] = stoneValue[left_index]
            right_max_value[left_index][left_index] = stoneValue[left_index]
            
            #用于计算线段总值
            total_value = stoneValue[left_index]
            
            #用于存储左侧线段的总值
            sum_left = 0
            
            #i用于标记分割节点
            # 判断最好的分割节点的方法是，刚好左侧的值大于右侧的值；那么索引减1就是分割点（左侧小于右侧值）
            i = left_index - 1
            #仅有1个石子时，值为0，无需计算
            #所以右侧边界，从第2个值开始
            for right_index in range(left_index + 1, num_of_stones):
                #累加计算出线段的值
                total_value += stoneValue[right_index]
                #找出分割点i，多一个值，就会导致左侧大于右侧；该点就是分割点
                while i + 1 < right_index and (sum_left + stoneValue[i + 1]) * 2 <= total_value:
                    #左侧值累加
                    sum_left += stoneValue[i + 1]
                    i += 1    
                #在状态转移中，如果sum(stoneValue [left_index: i ]) < sum(stoneValue [i + 1: right_index+1]) ，那么Bob会丢弃右侧部分，
                # 状态转移方程为f[left_index][right_index] = f[left_index][i] + sum(stoneValue [left_index: i + 1]) ，预存在left_max_value中
                #如果两个值的情况，left_index等于i
                if left_index <= i:
                    #由于i的值在滑动，所以要和自己比仅保留最大值；取i值为分割值时，才去右侧的值，所以到i结束
                    max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index], left_max_value[left_index][i])
                #在状态转移中，如果sum(stoneValue [left_index: i + 1]) > sum(stoneValue [i + 1: right_index +1]) ，那么Bob会丢弃左侧部分，
                # 状态转移方程为f[left_index][right_index] = f[i+1][right_index+1]+ sum(stoneValue [i + 1: right_index +1])  ，预存在right_max_value中
                if i + 1 < right_index:
                    #在第i+1个位置分割，才会取右侧线段值；所以求和从i+2开始
                    max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index], right_max_value[i+2][right_index])
                #在状态转移方程中，如果sum(stoneValue [left_index: i + 1]) == sum(stoneValue [i + 1: right_index])，那么Alice选择一个最有利的选项。
                # f[left_index][right_index] = max(f[left_index][i], f[i+1][right_index])+ sum(stoneValue [left_index: i + 1]) 
                #比较预存在预存在left_max_value和，预存在right_max_value中的值，i为分割位置，取大值
                if sum_left * 2 == total_value:
                    max_stone_value[left_index][right_index] = max(max_stone_value[left_index][right_index], max(left_max_value[left_index][i], right_max_value[i+1][right_index]))
                
                #计算左侧和右侧的最大值
                #在状态转移中，假设线段[left_index, right_index], 分割点为i；如果 sum(left_index,i)<sum(i+1,right_index)，那么有状态转移方程：
                # f[left_index][right_index]=f[left_index][i]+sum(left_index,i)
                # 而对于right_index +1而言，sum(left_index,i)<sum(i+1,right_index+1) 一定也成立，那么有状态转移方程：
                # f[left_index][right_index+1]=f[left_index][i]+sum(left_index,i) 
                # 基于上述分析，left_max_value[left_index][right_index] = max{max_stone_value[left_index][i] + sum(stone_value[left_index, i + 1]} i ∈ left_index~right_index
                # 如果是递推的方式表达，就是：left_max_value[left_index][right_index] = max{max_stone_value[left_index][right_index-1],  max_stone_value[left_index][right_index] + sum(stone_value[left_index, right_index + 1]}
                left_max_value[left_index][right_index] = max(left_max_value[left_index][right_index - 1], total_value + max_stone_value[left_index][right_index])  
                #右侧是同样的推理方式，不再赘述               
                right_max_value[left_index][right_index] = max(right_max_value[left_index + 1][right_index], total_value + max_stone_value[left_index][right_index])
        #最长线段的取值，就是Alice获取的最大值。
        return max_stone_value[0][-1]       
       

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