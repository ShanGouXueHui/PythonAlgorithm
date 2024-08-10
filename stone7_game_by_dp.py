#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int        
        
        #Author: ShanGouXuehui
        #Date: 2024-8-10
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        num_of_stones = len(stones)
        
        #计算累计值, 倒序计算，左侧多预留一个值，方便计算
        accumulate_value = [0 for _ in range(num_of_stones + 1)]
              
        for index in range(num_of_stones):
            accumulate_value[index + 1] = accumulate_value[index] + stones[index]
        
        #定义dp数组，用于存储最大差值
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备, n代表石子数）
        # 当只有1石子的时候，无剩余值，差值为0：f[n-1] [n-1] = 0
        # 加上求最大值，所以初始化为0
        max_different_value = [[0] * num_of_stones for _ in range(num_of_stones)]
        #从第2个石子开始，才能取到剩余值，才能有差值
        for left_index in range(num_of_stones - 2, -1, -1):
            for right_index in range(left_index+1, num_of_stones):
                #归纳递推（状态转移方程）
                # 区间为[left_index, right_index] 时，取值：
                # f[left_index, right_index] = max（sum(stones[left_index +1:right_index) - f[left_index + 1, 
                # right_index]，sum(stones[left_index:right_index -1) - f[left_index, right_index - 1]）
                # 为了复用值，剩余值求和，使用累计值相减得到
                max_different_value[left_index][right_index] = max(accumulate_value[right_index + 1] - accumulate_value[left_index + 1] - max_different_value[left_index + 1][right_index], accumulate_value[right_index] - accumulate_value[left_index] - max_different_value[left_index][right_index - 1])
            
        
        #最终返回最长的完整线段的最大得分
        return max_different_value[0][num_of_stones-1]   

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    stones = [5,3,1,4,2]
    # 输出：6
    print('示例1：', cs.stoneGameVII(stones))
    
    # 示例 2：
    # 输入：
    stones = [7,90,5,1,100,10,10,2]
    # 输出：122
    print('示例2：', cs.stoneGameVII(stones))