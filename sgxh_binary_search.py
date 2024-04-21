#-*- coding:utf-8 -*-

#二分查找算法实例 - 俄罗斯套娃信封问题
# 1) 套信封，有两个维度：宽和高
# 2) 我们先将“高”升序排序，同样高的信封，按照“宽”降序排序(同样宽或者高的信封，无法套在一起，降序可以天然避免同高，不等宽的信封做额外是否可以“套”的处理)
# 3) 基于第2步的“有序序列”，将“最多能有多少个信封”转化为了求“最长子序列问题”
# 4) 使用二分查找方法，查找套信封子序列的最大长度

def binary_search_evelopes(ev_list:list[int]):
    #先将信封按照宽升序、高降序，排序，将“最多能有多少个信封”转化为了求“最长子序列问题”
    #envelopes[i] = [wi, hi]
    ev_list = sorted(ev_list, key=lambda x:(x[0], -x[1]))
    
    # print('sorted list:', ev_list)
    
    #使用二分查找方法，求取套信封子序列的最大长度
    max_ASC_list = []
    for val in ev_list:
        #定义最长子序列，二分查找的前后滑动指针
        left_index = 0
        right_index = len(max_ASC_list)
        #在max_ASC_list中通过二分查找，求取最长子序列长度
        while(left_index < right_index):
            #获取中间值的索引，折半查找开始
            mid_index = left_index + ((right_index - left_index)//2)
            #取当前值，用于max_ASC_list中折半查找
            #由于宽是有序的，所以只需比较高即可
            current_value = val[1]
            
            #如果等于中位值，则已命中，终止循环
            if(max_ASC_list[mid_index] == current_value ):
                left_index = mid_index
                break   
            #如果当前信封的高大于中位值，则将在右侧区域继续比较，则滑动左侧索引
            elif(max_ASC_list[mid_index] < current_value):
                left_index = mid_index + 1
            #反之则在左侧区域继续比较
            else:
                right_index = mid_index - 1
        
        # print('ev_list[i][0] =', val[1])
        #如果当前元素值大于子序列中最大的值，则加入最大子序列      
        if left_index == len(max_ASC_list): 
            max_ASC_list.append(val[1])
        #如果比当前子序列中的值小，则替换子序列的值；
        #1、替换并不会导致子序列长度增长，因为他不比最外层的信封更大，无法再套一层
        #2、替换为更小的值，是由于后续的值比更小的值来说，更可能加入最大子序列（套信封更容易）
        else:
            max_ASC_list[left_index] = val[1]
            
    return len(max_ASC_list)


if __name__ == '__main__':
    #示例 1
    #输入
    ev_list = [[5,4],[6,4],[6,7],[2,3]]
    #输出：3, 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]
    print(binary_search_evelopes(ev_list))
    
    #示例 2
    #输入
    ev_list = envelopes = [[1,1],[1,1],[1,1]]
    #输出：1
    print(binary_search_evelopes(ev_list))
    
    
    #示例 3
    #输入
    ev_list = [[5,4],[6,4],[6,7],[2,1],[3,3],[6,4],[6,8],[7,9]]
    #输出：5, 最多信封的个数为 5, 组合为: [2,1] => [3,3]=> [5,4] => [6,7] => [7,9]
    print(binary_search_evelopes(ev_list))