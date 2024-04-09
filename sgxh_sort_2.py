#-*- coding:utf-8 -*-
import time
import random

def shell_sort(raw_list:list[int]):
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('shell_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list)
    
    shell_sort_length = len(raw_list)
    #获取比较步长
    gap = shell_sort_length//2
    #分解子序列进行分别排序，直到子序列为1个
    while gap > 0:
        #从步长元素的下一个元素开始比较
        for i in range(gap, shell_sort_length):
            #临时存储用于比较的元素值
            tmp = raw_list[i]
            j = i
            #针对该元素值进行插入排序，由于前面的数已经是有序的了（从小到大的顺序）
            #仅需将当前元素按照直接插入的方式插入有序的位置即可
            #raw_list[j - gap]是下标索引小的位置的值，所以如果大于目标值，则交换位置
            while j >= gap and raw_list[j - gap] > tmp:
                raw_list[j] = raw_list[j - gap] 
                #仅比较同一个子序列里面的值即可
                j -= gap
            raw_list[j] = tmp
        gap = gap//2
    end_time = time.time()*1000
    print('shell_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)
   
    
    print('shell_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')

def merge_sort(raw_list:list[int]):
    merge_sort_length = len(raw_list)
    #如果仅有一个元素，已经是有序的，则直接返回
    if merge_sort_length <= 1:
        return raw_list
    #将要判断的序列分成两个队列，进行排序和合并
    mid = merge_sort_length//2
    return merge(merge_sort(raw_list[:mid]), merge_sort(raw_list[mid:]))

#将两个排序的列表合并成一个列表
def merge(raw_list1:list[int], raw_list2:list[int]):
    #结果存储列表
    merge_result = []
    
    #将两个有序（从小到大）的列表逐个合并
    #从只有1个元素的序列开始，就是有序的序列，所以后续的序列都是有序的。
    while raw_list1 and raw_list2:
        if raw_list1[0] < raw_list2[0]:
            merge_result.append(raw_list1.pop(0))
        else:
            merge_result.append(raw_list2.pop(0))
    #处理两个队列不等长的情况
    if raw_list1:
        merge_result += raw_list1
    if raw_list2:
        merge_result += raw_list2
    #返回合并后的队列
    return merge_result

#堆排序
def heap_sort(raw_list:list[int]):
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('heap_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list)
    
    merge_sort_length = len(raw_list)
    
    #构建一个大顶锥，从非叶子节点开始，将大值浮出来,确定根节点是最大值
    #原理：在二叉树中，如果深度由K，那么整个树最多有2^k - 1个节点(2^k - 1) - (2^(k-1) - 1)) = (2^k - 1)/2
    for i in range(merge_sort_length//2 - 1, -1, -1):
        heap_tree(raw_list, merge_sort_length, i)
        
    #确保根节点是最大值，然后将根节点依次放在最后一个位置，最终得到有序列表
    for i in range(merge_sort_length - 1, 0,- 1):
        raw_list[i], raw_list[0] = raw_list[0], raw_list[i] 
        #不考虑已经排序出来的最值们，所以长度变为i       
        heap_tree(raw_list, i, 0)
    
    end_time = time.time()*1000
    print('heap_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)       
    print('heap_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')

#二叉树可以使用List来表示,原理：在二叉树中的第i层，最多由2^(i-1)的节点
def heap_tree(raw_list:list[int], merge_sort_length:int, index:int):
    #根是最大值, 初始化
    lagest_value_index = index
    
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    
    #如果左子节点存在且大于根节点
    if left_child_index < merge_sort_length \
        and raw_list[left_child_index] > raw_list[lagest_value_index]:
            lagest_value_index = left_child_index
            
    #如果右子节点存在且大于根节点
    if right_child_index < merge_sort_length \
        and raw_list[right_child_index] > raw_list[lagest_value_index]:
            lagest_value_index = right_child_index
    
    #如果最大节点不是根节点,做相应节点交换，保证根节点是最大值
    if lagest_value_index != index:
        raw_list[index], raw_list[lagest_value_index] = raw_list[lagest_value_index], raw_list[index]    
        #子节点重新排序
        heap_tree(raw_list, merge_sort_length, lagest_value_index)

#快速排序算法
def quick_sort(raw_list:list[int], low_partition_index:int, high_partition_index:int):
    #如果低值区和高级区重合，则直接返回
    if low_partition_index >= high_partition_index:
        return raw_list
    #取第1个值为基准值
    pivot = raw_list[low_partition_index]
    #定义指针，用于滑动处理值
    low = low_partition_index
    high = high_partition_index
    while low < high:
        #从右向左扫描，获取小于基准值的元素
        while low < high and raw_list[high] >= pivot:
            high -= 1
        raw_list[low] = raw_list[high]
        #从左向右扫描吗，获取大于基准值的元素
        while low < high and raw_list[low] <= pivot:
            low += 1
        raw_list[high] = raw_list[low]
    #中间值设置，低值区索引和高值取索引相遇，中间值就是基准值的位置
    raw_list[high] = pivot
    #低值区和高值区分开计算，快速排序
    quick_sort(raw_list, low_partition_index, low-1)
    quick_sort(raw_list, low + 1, high_partition_index)
    return raw_list

if __name__ == '__main__':
    #实例
    #输入参数生成
    raw_list1 = []
    raw_list2 = []
    raw_list3 = []
    raw_list4 = []
    for i in range(2000):
        raw_list1.append(i)
        raw_list2.append(i)
        raw_list3.append(i)
        raw_list4.append(i)
        
    random.shuffle(raw_list1)
    shell_sort(raw_list1)
    
    #记录开始时间，用于计算排序时长
    random.shuffle(raw_list2)
    start_time = time.time()*1000
    print('merge_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list2)    
  
    raw_list2 = merge_sort(raw_list2)
    
    end_time = time.time()*1000
    print('merge_sort sorting end time: ', end_time)    
    
    # print('sorted_list : ', raw_list2)
    print('merge_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')
    
    random.shuffle(raw_list3)
    heap_sort(raw_list3)
    
    
    #记录开始时间，用于计算排序时长
    random.shuffle(raw_list4)
    start_time = time.time()*1000
    print('quick_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list4)    
  
    raw_list4 = quick_sort(raw_list4, 0, len(raw_list4) - 1)
    
    end_time = time.time()*1000
    print('quick_sort sorting end time: ', end_time)    
    
    # print('sorted_list : ', raw_list4)
    print('quick_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')
    