#-*- coding:utf-8 -*-

import time
import random

#冒泡排序
def bubble_sort(raw_list:list):
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('bubble_sort sorting start time: ', start_time)
    # print('raw_list : ', raw_list)
    raw_list_length = len(raw_list)
    #从第一个元素开始，一次遍历
    for i in range(1, raw_list_length):
        #i表示第i个选出的最大值，(i, raw_list_length)是依次已排序好的元素
        for j in range(0, raw_list_length - i):
            if raw_list[j] > raw_list[j+1]:
                raw_list[j], raw_list[j+1] = raw_list[j+1],raw_list[j]
    
    end_time = time.time()*1000
    print('bubble_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)
   
    
    print('bubble_sort耗费时长(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')

#选择排序 
def selection_sort(raw_list:list):
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('selection_sort sorting start time: ', start_time)
    # print('raw_list : ', raw_list)
    raw_list_length = len(raw_list)
    #从第一个元素开始，一次遍历；剩余最后一个元素的时候，肯定是最值，无需进一步处理
    for i in range(raw_list_length-1):
        min_index = i
        #（0,i）表示一次已经选择出来的最小值，不再重复看
        for j in range(i+1, raw_list_length):
            if raw_list[j] < raw_list[min_index]:
                min_index = j
            
            if i != min_index:
                raw_list[i], raw_list[min_index] = raw_list[min_index],raw_list[i]
    end_time = time.time()*1000
    print('selection_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)
    
    
    print('selection_sort(MS): ', (end_time - start_time))
    print('------------------------------------------------------------')
    
#插入排序
def insertion_sort(raw_list:list):
    #记录开始时间，用于计算排序时长
    start_time = time.time()*1000
    print('insertion_sort sorting start time: ', start_time)
    # print('raw_list : ', raw_list)
    raw_list_length = len(raw_list)
    
    for i in range(1, raw_list_length):
        #已排序和未排序分解点，索引标识；默认第1个元素是已经排序的，从第二个元素开始
        sorted_flag = i - 1
        #设置一个临时值，用于交换存储位置
        current_element = raw_list[i]    
        #扫描已经排序的序列，将新元素插入到合适的位置   
        while True:
            if (sorted_flag < 0):
                break
            #从排序序列的最大值开始对比，如果大于目标值，那么存储位置向后延续1位
            if raw_list[sorted_flag] > current_element:
                raw_list[sorted_flag + 1],raw_list[sorted_flag] = raw_list[sorted_flag],raw_list[sorted_flag + 1]
                sorted_flag -= 1
            #如果遇到了小于等于目标值的位置，那么直接将空闲值设置为当前值
            else:
                raw_list[sorted_flag + 1] = current_element
                break         
    end_time = time.time()*1000
    print('insertion_sort sorting end time: ', end_time)
    # print('sorted_list : ', raw_list)
    
    
    print('insertion_sort(MS): ', (end_time - start_time))

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
    random.shuffle(raw_list2)
    random.shuffle(raw_list3)
    bubble_sort(raw_list1)
    selection_sort(raw_list2)
    insertion_sort(raw_list3)