#-*- coding:utf-8 -*-


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-09-10
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        
        #获得元素个数，用于后续复用
        num_of_elements = len(nums)
        #初始位置为 nums[0]
        if num_of_elements == 1:
            return 0
        
        
        #当前跳和下一跳到达最远的位置, 从第一个位置开始
        current_hop_reached_position = nums[0]
        next_hop_farest_position = nums[0]
        
        
        #所需最小跳数，起点为nums[0], 初始化为1
        num_of_hops = 1
        
        #3、依次类推，直到到达nums[n-1]，即可计算出需要几跳    
        for position in range(1, num_of_elements):
            if current_hop_reached_position >= position:
                
                #如果已经到达了最后一个位置，则直接停止
                if current_hop_reached_position >= num_of_elements - 1:
                    break
                
                #2、我们只需在num[i]的基础上，在num[i]~num[i + j]选择，叠加后跳的最远的位置，作为第2跳。
                next_hop_farest_position = max(next_hop_farest_position, position + nums[position])  
                
                #1、假设num[i]的值为j，那么num[i]~num[i + j]的位置一跳可达，如果超过num[i + j]，那么就需要第2跳。
                if position == current_hop_reached_position:                    
                    current_hop_reached_position = next_hop_farest_position
                    num_of_hops += 1
        return num_of_hops

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    nums = [2,3,1,1,4]
    # 2
    print('示例1： ', cs.jump(nums))
    
    # 示例 2：
    # 输入：1
    nums =[2,1]
    # 输出1
    print('示例2： ', cs.jump(nums))
    
    # 示例 3：
    # 输入：
    nums = [0]
    # 输出0
    print('示例3： ', cs.jump(nums))
    
    # 示例 4：
    # 输入：
    nums = [1, 2]
    # 输出1
    print('示例4： ', cs.jump(nums))