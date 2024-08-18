#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int   
        
        #Author: ShanGouXuehui
        #Date: 2024-8-18
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        num_of_stones = len(stones)
        
        #计算累计值, 倒序计算，左侧多预留一个值，方便计算
        accumulate_value = [0 for _ in range(num_of_stones)]
        
        accumulate_value[0] = stones[0]  
        for index in range(1, num_of_stones):
            accumulate_value[index] = accumulate_value[index - 1] + stones[index]
        
        #定义dp数组，用于存储最大差值
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备, n代表石子数）
        # 当只有1石子的时候，无剩余值，差值为0：f[n-1] [n-1] = 0
        # 加上求最大值，所以初始化为0
        max_different_value = [0] * num_of_stones
        # 归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备, n代表石子数）
        # 当取值为n-1，差值为所有石子之和：f[n-1]= accumulate_value[n-1]
        max_different_value[num_of_stones-1] = accumulate_value[num_of_stones-1]
        
        #倒数第1个石子为初始值，所以从倒数第2个石子开始
        for i in range(num_of_stones - 2, -1, -1):
            # 归纳递推（状态转移方程）
            # 取值为i时：f[i]=max(f[i+1], accumulate[i]−f[i+1])
            max_different_value[i] = max(max_different_value[i + 1], accumulate_value[i] - max_different_value[i + 1])
        
        #最少选取1个石子，所以最大值为: f[1]
        return max_different_value[1]   

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    stones = [-1,2,-3,4,-5]
    # 输出：5
    print('示例1：', cs.stoneGameVIII(stones))
    
    # 示例 2：
    # 输入：
    stones = [7,-6,5,10,5,-2,-6]
    # 输出：13
    print('示例2：', cs.stoneGameVIII(stones))
    
    # 示例 3：
    # 输入：
    stones = [-10,-12]
    # 输出：-22
    print('示例3：', cs.stoneGameVIII(stones))