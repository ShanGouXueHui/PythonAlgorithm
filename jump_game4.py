#-*- coding:utf-8 -*-


class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
                
        #Author: ShanGouXuehui
        #Date: 2024-09-22
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        #使用先入先出队列遍历所触达的节点
        from collections import defaultdict, deque
        
        #获得元素个数，用于后续复用
        num_of_elements = len(arr)
        
        #如果只有一个元素，不用动就可以到达
        if num_of_elements == 1:
            return 0
        
        #使用字典快速存取重复值的index, 同一个key，多个value，声明list类型的dict
        index_dict = defaultdict(list)
        
        #使用enumerate，取到下标
        for index, value in enumerate(arr):
            index_dict[value].append(index)
            
        #使用set（比list块），判断节点是否已经访问
        visited_index = set()          
        
        #定义先入先出队列，用于广度优先算法搜索（相邻位置，或者同值）
        #一开始在数组的第一个元素处（下标为 0），首先访问就是0位置
        visiting_queue = deque()
        visiting_queue.append([0,0])
        
        while visiting_queue:
            #每一步对应多个节点，所以取下标索引的时候，要重新取一下步数
            current_index, min_steps = visiting_queue.popleft()
            visited_index.add(current_index)
            min_steps += 1
            
            #每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j 
            # j需满足：arr[i] == arr[j] 且 i != j
            # 第一个确认步骤，查看i 跳到下标 i + 1;i + 1 需满足：i + 1 < arr.length
            if current_index + 1 < num_of_elements and (current_index + 1) not in visited_index:
                visited_index.add(current_index + 1)
                
                #如果已经达到了最后一个位置，则直接返回
                if current_index + 1 == num_of_elements - 1:
                    return min_steps
                #否则加入待访问遍历列表
                else:
                    visiting_queue.append([current_index + 1, min_steps])
                    
            #第二确认步骤，i跳i - 1 ；i - 1 需满足：i - 1 >= 0
            if current_index - 1 >= 0 and (current_index - 1) not in visited_index:
                visited_index.add(current_index - 1)
                #后退一个节点不可能是最后一个节点，所以直接加入待访问李彪
                visiting_queue.append([current_index - 1, min_steps])
            
            #第三确认步骤，跳到j；j需满足：arr[i] == arr[j] 且 i != j
            current_value = arr[current_index]
            for tmp_index in index_dict[current_value]:
                if tmp_index not in visited_index:
                    visited_index.add(tmp_index)
                    #如果已经达到了最后一个位置，则直接返回
                    if tmp_index == num_of_elements - 1:
                        return min_steps
                    #否则加入待访问遍历列表
                    else:
                        visiting_queue.append([tmp_index, min_steps])
            #将已经处理过的节点删除，避免重复处理
            del index_dict[current_value]
        #如果没有到达最后一个位置，则返回无穷大
        return float('inf')

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    # 输出：3
    # 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。 
    print('示例1： ', cs.minJumps(arr))
    
    # 示例 2：
    # 输入：
    arr = [7]
    # 输出：0
    # 解释：一开始就在最后一个元素处，所以你不需要跳跃。 
    print('示例2： ', cs.minJumps(arr))
    
    # 示例 3：
    # 输入：
    arr = [7,6,9,6,9,6,9,7]
    # 输出：1
    print('示例3： ', cs.minJumps(arr))