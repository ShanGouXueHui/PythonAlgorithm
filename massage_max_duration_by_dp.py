#-*- coding:utf-8 -*-

class Solution(object):
    def massage(self, nums):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-05
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type nums: List[int]
        :rtype: int
        """
        #获取预约次数，用于后续复用
        nums_length = len(nums)
        #如果没有预约，那么按摩时长为0，直接返回
        if nums_length < 1:
            return 0
        
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #第1个预约：f[n][0] = 0， f[n][1] = nums[0]
        #由于第n次预约的值，仅与n-1次的值相关，所以无需记录整个dp table，仅需记录上一次预约的最长按摩时间即可
        #f[n][0] = 0
        last_appointment_max_duration_reject = 0
        #f[n][1] = nums[0]
        last_appointment_max_duration_accept = nums[0]
        
        #归纳递推（状态转移方程）求解
        #第n天时：f[n][0] = max(f[n-1][0],f[n-1][1])，f[n][1] = f[n-1][0] + nums[n]
        for i in range(1, nums_length):
            #第n次预约不接，那么第n-1次预约，可以接也可以不接；所以f[n][0] = max(f[n-1][0],f[n-1][1])
            current_appointment_max_duration_reject = max(last_appointment_max_duration_reject, last_appointment_max_duration_accept)
            #第n次预约接了，那么第n-1次预约不能接受；所以f[n][1] = f[n-1][0] + nums[n]
            current_appointment_max_duration_accept = last_appointment_max_duration_reject + nums[i]
            #更新“n-1”的值，方便求n的值
            last_appointment_max_duration_reject, last_appointment_max_duration_accept = current_appointment_max_duration_reject, current_appointment_max_duration_accept
        #最终值，取max(f[n][0],f[n][1]）即是最终结果
        return max(last_appointment_max_duration_reject, last_appointment_max_duration_accept)
        
if __name__ == "__main__":
    cs = Solution()
    
    #示例 1
    # 输入
    nums = [1,2,3,1]
    # 输出： 4
    # 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4
    print('示例1：', cs.massage(nums))
    
    #示例 2
    # 输入
    nums = [2,1,4,5,3,1,1,3]
    # 输出： 12
    # 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12
    print('示例2：', cs.massage(nums))