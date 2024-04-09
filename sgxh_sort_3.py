#-*- coding:utf-8 -*-
import time
import random

def counting_sort(raw_list:list[int]):    
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('counting_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list)
    
    #定义变量存储数组中的最大值和最小值
    max = 0
    min = 9999999999999999 
    
    #获取最大值和最小值
    for i in raw_list:
        if i < min:
            min = i
        if i > max:
            max = i
    
    #外部计数序列,均初始化为0个元素
    external_counting_list = [0] * (max - min +1)
    
    #依次获取每个数字的数量，并存储在外部计数序列中
    #下标值 + min = list中的元素值；
    #external_counting_list对应下标的值，则是raw_list中同样大小的值的数量
    for val in raw_list:
        external_counting_list[val - min] += 1
    #按照external_counting_list每个元素的数量（值），依次存入raw_list，即完成排序
    #从下表推算值：下标值 + min = list中的元素值；
    #对应下标的元素的值，则是同样数值的个数
    tmp_index = 0
    for s in range(max - min +1):
        for c in range(external_counting_list[s]):
            raw_list[tmp_index] = s + min
            tmp_index += 1
    end_time = time.time()*1000
    print('counting_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)
   
    
    print('counting_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')       

def bucket_sort(raw_list:list[int]):    
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('bucket_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list)
    
    #定义变量存储数组中的最大值和最小值
    max = 0
    min = 9999999999999999 
    
    #获取最大值和最小值
    for i in raw_list:
        if i < min:
            min = i
        if i > max:
            max = i
    
    #桶的大小,默认桶的个数为raw_list元素个数，那么单个桶的大小 = 区间值/桶数
    bucket_size = (max - min)/len(raw_list)
    
    #定义外部存储数组，一维是桶数，二维是桶内元素
    external_bucket_list = [[] for i in range(len(raw_list) + 1)]
    
    #按照区间，将raw_list中的元素值，填充到桶内
    for val in raw_list:
        #桶的大小都是一样的，根据raw_list中元素的值，可以推算出第几个桶：((i - min)//bucket_size)
        #然后将元素放在该桶的List中
        external_bucket_list[int((val - min)//bucket_size)].append(val)
    #清空结果list，方便回填
    raw_list.clear()
    #将非空桶排序，然后放入有序的List中；桶内排序我们使用快速排序算法：quick_sort(bucket_list, 0, len(bucket_list) - 1)
    for bucket_list in external_bucket_list:
        if bucket_list:
            # print(bucket_list)
            for j in quick_sort(bucket_list, 0, len(bucket_list) - 1):
                raw_list.append(j)
    
    end_time = time.time()*1000
    print('bucket_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)   
    
    print('bucket_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------') 
    
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

def radix_sort(raw_list:list[int]):
     #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('radix_sort sorting start time: ', start_time)    
    # print('raw_list : ', raw_list)
    
    #定义变量存储数组中的最大值
    max = 0
    
    #获取最大值
    for i in raw_list:
        if i > max:
            max = i
    #获取最大位数
    max_digit = len(str(max))
    
    #按照个/十/百/千/万...的位数顺序，诸位的排序
    for i in range(max_digit):
        #每一位数字取值范围均为0~9，故建立10个桶
        bucket_list = [[] for i in range(10)]
        #按照第i位数，放入对应序号的桶中
        for j in raw_list:
            #通过10**i，取第i位的数字
            bucket_list[j//(10**i)%10].append(j)
        #按照桶的顺序，来调整raw_list中元素的顺序,用于下一位的比较
        raw_list =[val for digit_list in bucket_list for val in digit_list]

    end_time = time.time()*1000
    print('radix_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)   
    
    print('radix_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------') 
    
    return raw_list

if __name__ == '__main__':
    #实例
    #输入参数生成
    raw_list1 = []
    raw_list2 = []
    raw_list3 = []  
    for i in range(2000):
        raw_list1.append(i)
        raw_list2.append(i)
        raw_list3.append(i)
    
    random.shuffle(raw_list1)
    counting_sort(raw_list1)
    
    random.shuffle(raw_list2)
    bucket_sort(raw_list2)
    
    random.shuffle(raw_list3)
    radix_sort(raw_list3)