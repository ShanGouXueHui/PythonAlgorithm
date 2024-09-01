#-*- coding:utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        #Author: ShanGouXuehui
        #Date: 2024-09-01
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获得元素个数，用于后续复用
        num_of_elements = len(nums)
        #到达最远的位置, 从第一个位置开始
        reach_farest_position = 0
        
        for position_index in range(num_of_elements):
            #如果可以到达当前位置，则继续往下跳跃
            if reach_farest_position >= position_index:
                #当前位置可以到达的最远位置为position_index + nums[position_index]
                #历史最远，和本位置最远，做一个比较，保留更远的值
                reach_farest_position = max(reach_farest_position, position_index + nums[position_index])
                #如果到达终点返回True
                if reach_farest_position >= num_of_elements - 1:
                    return True
            #如果没有到达当前位置，则游戏结束
            else:
                return False
                
        #最终没有到达最后一个位置
        return False
        

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    nums = [2,3,1,1,4]
    # 输出：true
    # 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
    print('示例1： ', cs.canJump(nums))
    
    # 示例 2：
    # 输入：
    nums = [3,2,1,0,4]
    # 输出：false
    # 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
    print('示例1： ', cs.canJump(nums))