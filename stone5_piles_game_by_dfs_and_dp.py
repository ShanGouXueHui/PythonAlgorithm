#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        
        #超时
        
        #Author: ShanGouXuehui
        #Date: 2024-7-31
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        
        #计算累计值
        num_of_stones = len(stoneValue) 
        accumulate_value = [0 for _ in range(num_of_stones)]
        
        accumulate_value[0] = stoneValue[0]        
        for index in range(1, num_of_stones):
            accumulate_value[index] = accumulate_value[index-1] + stoneValue[index]
            
        best_accumulate_value = self.get_best_value_by_dfs(0, num_of_stones - 1, stoneValue, accumulate_value)
        return best_accumulate_value
    
    def get_best_value_by_dfs(self, left_index, right_index, stoneValue, accumulate_value):
            #如果仅剩一个石子，游戏接入，不增加值
            if left_index == right_index:
                return 0   
            
            #求出左侧线段的值之和，用于后续代码复用
            left_segment_total_value = 0
            #记录最终值
            best_accumulate_value = 0
            #分割点起始与左侧第一个值（相当于左侧线段仅有一个值），
            # 结束与最后一个值之前（如果到了最右侧一个值，相当于没有分割线段）
            for i in range(left_index, right_index):
                if left_index == 0:
                    left_segment_total_value = accumulate_value[i]
                else:
                    left_segment_total_value = accumulate_value[i] - accumulate_value[left_index - 1]
                right_segment_total_value = accumulate_value[right_index] - accumulate_value[i]
                
                if left_segment_total_value < right_segment_total_value:
                    best_accumulate_value = max(best_accumulate_value, self.get_best_value_by_dfs(left_index, i, stoneValue,accumulate_value) + left_segment_total_value)
                elif left_segment_total_value > right_segment_total_value:
                    best_accumulate_value = max(best_accumulate_value, self.get_best_value_by_dfs(i+1, right_index,stoneValue,accumulate_value) + right_segment_total_value)
                else:
                    best_accumulate_value = max(best_accumulate_value, max(self.get_best_value_by_dfs(left_index, i, stoneValue,accumulate_value) + left_segment_total_value, self.get_best_value_by_dfs(i+1, right_index,stoneValue,accumulate_value) + right_segment_total_value))
                    
            return best_accumulate_value
    
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