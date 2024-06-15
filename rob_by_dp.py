#-*- coding:utf-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-05
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type nums: List[int]
        :rtype: int
        """
        
        #获取房间个数，用于后续复用
        no_of_rooms = len(nums)
        
        #如果只有一个房间，没得选
        if no_of_rooms == 1:
            return nums[0]
        
        #由于第i个值仅和第i-1和i-2有关系，所以定义两个值用于存储历史值即可
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）        
        # 处于第1个房间(下标0)的时候，无连续房间：f(0) = nums[0]
        last_1_best_amount = nums[0]
        # 处于第2个房间的时候，两个房间连续，只能选一个大值：f(1) = max(nums[0], nums[1])
        last_2_best_amount = max(nums[0],nums[1])
        
        #如果只有2个房间，返回两个中的大值
        if no_of_rooms == 1:
            return last_2_best_amount
                
        #归纳递推（状态转移方程）
        # 假设偷窃到了第i个房间，那么最大现金取值有两种“选择”：从第i-1偷窃了现金，那么无法从第i个房间继续偷窃，则f(i) = f(i-1); 未从第i-1偷窃现金，那么，就可以从i-2跳到本房间偷窃现金，则金额为f(i) = f(i-2) + nums[i]
        #第i天时：f(i) = max( f(i-1), f(i-2) + nums[i])
        for i in range(2, no_of_rooms):
            #按照递推方程，求出截止当前房间，可以盗窃出最高额的现金值
            room_i_best_amount = max(last_2_best_amount, last_1_best_amount + nums[i])
            #重设第i-1和i-2的值
            last_1_best_amount, last_2_best_amount = last_2_best_amount, room_i_best_amount
        
        #返回第no_of_rooms个房间的最高值
        return last_2_best_amount
            
  

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入
    nums = [1,2,3,1]
    # 输出：4
    # 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    #      偷窃到的最高金额 = 1 + 3 = 4 。
    print('示例1：', cs.rob(nums))
    
    # 示例 2
    # 输入
    nums =  [2,7,9,3,1]
    # 输出：12
    # 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    #      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    print('示例2：', cs.rob(nums))