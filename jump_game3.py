#-*- coding:utf-8 -*-


class Solution(object):
    def canReach(self, arr, start):        
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
                
        #Author: ShanGouXuehui
        #Date: 2024-09-18
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        #使用先入先出队列遍历所触达的节点
        from collections import deque
        
        #获得元素个数，用于后续复用
        num_of_elements = len(arr)
        #初始位置为 0,则直接返回
        if arr[start] == 0:
            return True
        
        #记录是否已经check过，dict比list判断更有效率，使用dict做not in判断
        checked_list = {start}
        #使用queue依次遍历所能触达的节点
        checking_queue = deque([start,])
        
        #使用while循环，遍历所能触达节点
        while checking_queue:
            #取出最先放入队列的元素
            check_point = checking_queue.popleft()
            #当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]
            #如果超出边界，则无需处理；负责检查一下是否满足true的条件
            for p_index in [check_point - arr[check_point],check_point + arr[check_point]]:
                if (0 <= p_index and p_index < num_of_elements) and (p_index not in checked_list):
                    if arr[p_index] == 0:
                        return True 
                    #如果当前条件不满足True的条件，则加入队列，逐个遍历
                    checking_queue.append(p_index)
                    #当前节点放入checked list，避免重复check
                    checked_list.add(p_index)
        #如果遍历完全，人不满足，则直接返回false
        return False

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    arr = [4,2,3,0,3,1,2]
    start = 5
    # 输出：true
    # 解释：
    # 到达值为 0 的下标 3 有以下可能方案： 
    # 下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
    # 下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 
    print('示例1： ', cs.canReach(arr, start))
    
    # 示例 2：
    # 输入：1
    arr = [4,2,3,0,3,1,2]
    start = 0
    # 输出 true
    print('示例2： ', cs.canReach(arr, start))
    
    # 示例 3：
    # 输入：
    arr = [3,0,2,1,2]
    start = 2
    # 输出false
    print('示例3： ', cs.canReach(arr, start))