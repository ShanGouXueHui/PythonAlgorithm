#-*- coding:utf-8 -*-
'''
需求: 给定一个字符串 target_string(由英文字母、数字、符号和空格组成)，找出其中不含有重复字符的最长子串的长度和内容。
用例 1:
输入: target_string = "a123accdb"
输出: 4 , a123
用例 2:
输入: target_string = "b aa1122"
输出: 2, b 
用例 3:
输入: target_string = "ooooooo"
输出: 1, o
'''

def find_longest_str_window(target_string:str):
    #定义窗口边界，初始化为第1个字符
    left_index = 0
    right_index = 0
    
    #存储最优解，保存在list，方便获取重复字符的下标；初始化为第1个字符
    current_result = [target_string[left_index],]
    current_result_length = 1
    best_result = [target_string[left_index],]
    best_result_length = 1
    
    #打印初始化窗口
    show_sliding_window(target_string, left_index, right_index)
    
    #窗口滑动逻辑，时间复杂度O(n)
    target_string_length = len(target_string)
    while True:
        #窗口向右滑动一个位置，如果超出目标字符串长度，则标识处理完成，退出循环
        right_index = right_index + 1
        if right_index >= target_string_length:
            break
        #如果即将加入窗口的字符，与当前窗口无重复字符，则加入窗口
        if not (target_string[right_index] in current_result):
            current_result.append(target_string[right_index])
            current_result_length = current_result_length + 1
            
            #由于滑动窗口有变化，需要判断是否更新最优解
            if best_result_length < current_result_length:
                best_result = target_string[left_index:right_index+1]
                best_result_length = len(best_result)
                #打印新窗口位置
                show_sliding_window(target_string, left_index, right_index)
        #如果即将进入窗口的字符在旧窗口中有重复字符，则左侧边界left_index则挪至重复字符的下一个字符位置
        #同时将新字符加入窗口
        #由于新窗口最多和最优解一样长度，所以最优解值无变化
        else:
            left_index = left_index + current_result.index(target_string[right_index]) + 1
            current_result= list(target_string[left_index:right_index+1])
            current_result_length = len(current_result)
    #处理完成后打印最终结果
    print('无重复最长字符串长度与字符为：', best_result_length, best_result)
            
     
        
#为演示窗口滑动过程，定义一个格式话打印函数，使用[]标出最优解的变化
def show_sliding_window(target_string:str, left_index:int, right_index:int):
    if left_index == 0:
        print('[',target_string[left_index:right_index+1],']',target_string[right_index+1::])
    elif right_index == 0:
        print(target_string[0:left_index],'[',target_string[left_index:right_index+1],']')
    else:
        print(target_string[0:left_index],'[',target_string[left_index:right_index+1],']',target_string[right_index+1::])


if __name__ == '__main__':    
    #输出: 5 , 123ac
    target_string = "a123accdb"
    find_longest_str_window(target_string)
    
    #输出: 3, b_a
    target_string = "b_aa1122"
    find_longest_str_window(target_string)
    
    #输出: 1, o
    target_string = "ooooooo"
    find_longest_str_window(target_string)