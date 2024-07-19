#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        
        #Author: ShanGouXuehui
        #Date: 2024-7-19
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获取石子堆数，用于后续的代码复用        
        num_of_piles = len(piles)
        
        #由于可以从两端取值，那么我们可以通过左右指针，
        #来标识左右各有哪些石子堆被取走了，我们记为: left_pile_index, right_pile_index
        left_pile_index = 0
        right_pile_index = num_of_piles - 1 
        
        #由于需要记录上次和本次最大值索引，提前预定义; 从0次选择开始
        max_pile_index = 0
        last_pile_index = 0
        
        #定义dp数组, 定义顺序是返的，先定义player维度；再定义石块堆数维度，因为定义了从0次开始，所以长度要+1
        max_stones_count = [[0 for _ in range(2)] for _ in range(num_of_piles + 1)]
        
        
        #归纳递推（状态转移方程）
        #第i次选择时(dp数组从0开始，所以下标+1)：
        # f[max_pile_index + 1][0] = f（last_pile_index） + piles[max_pile_index] , 
        # f[max_pile_index + 1][1] =  f（last_pile_index） 或者反过来。
        # 其中：max_pile_index = left_index if difference_left > difference_right，反之则是right_index
        visited_count = 1
        while visited_count <= num_of_piles:
            # 假设玩家1选择开始，那么玩家2最大值是max_left，求个相差值。
            max_left = piles[left_pile_index] - max(piles[left_pile_index + 1], piles[right_pile_index])
            #假设玩家1选择末尾位置，那么玩家2最大值是max_right，求个相差值。
            max_right = piles[right_pile_index] - max(piles[left_pile_index], piles[right_pile_index - 1])
            
            #如果difference_left > difference_right那么此时玩家1应该选择开始位置的值，
            # 使得玩家2获取的石子数最小；反之选择末尾位置。
            if max_left >= max_right:
                max_pile_index = left_pile_index
            else:
                max_pile_index = right_pile_index
            
            #归纳递推（状态转移方程）
            # 第i次选择时(dp数组从0开始，所以下标+1)：
            # f[max_pile_index + 1][0] = f（last_pile_index） + piles[max_pile_index] , 
            # f[max_pile_index + 1][1] =  f（last_pile_index） 或者反过来。
            # 其中：max_pile_index = left_index if difference_left > difference_right，反之则是right_index
            if visited_count%2 == 1:
                max_stones_count[max_pile_index + 1][0] = max_stones_count[last_pile_index][0] + piles[max_pile_index] 
                max_stones_count[max_pile_index + 1][1] = max_stones_count[last_pile_index][1]
            else:
                max_stones_count[max_pile_index + 1][1] = max_stones_count[last_pile_index][1] + piles[max_pile_index] 
                max_stones_count[max_pile_index + 1][0] = max_stones_count[last_pile_index][0]
            
                
            last_pile_index = max_pile_index + 1
            visited_count += 1
        #当 Alice 赢得比赛时返回 true ，当 Bob 赢得比赛时返回 false 。
        if max_stones_count[max_pile_index + 1][0] >= max_stones_count[max_pile_index + 1][1]:
            return True
        else:
            return False

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    piles = [5,3,4,5]
    # 输出：true
    print('示例1：', cs.stoneGame(piles))
    
    # 示例 2
    # 输入
    piles = [3,7,2,3]
    # 输出：true
    print('示例2：', cs.stoneGame(piles))
    
    # 示例 3
    # 输入
    piles = [1,6,6,9,8,10,5,4]
    # 输出：true
    print('示例3：', cs.stoneGame(piles))
    
        