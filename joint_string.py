#-*- coding:utf-8 -*-

#Author: ShanGouXuehui
#Date: 2024-5-26
#Git: https://github.com/ShanGouXueHui/PythonAlgorithm
#Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
#Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        return self.find_joint_string_by_slide_window(s,words)
    
    #增加可读性，自己定义一个独立方法来完成算法
    def find_joint_string_by_slide_window(self, raw_string:str, words:list[str]) -> list[int]:
        #定义返回结果，并初始化
        result_index_list  = []
        #算出原始串长度，words中单词数量以及单词长度，串联字符串长度，用于后续代码复用
        raw_string_length = len(raw_string)
        no_of_words = len(words)         
        single_word_length = len(words[0])
        joint_word_length = single_word_length * no_of_words
        
        #如果串联字符串大于原始字符串，那么结果肯定为0，直接返回
        if joint_word_length > raw_string_length:
            return result_index_list
        
        #定义滑动窗口的边界指针
        slide_window_left_index = 0
        slide_window_right_index = slide_window_left_index + joint_word_length
        
        #串联字符串求解模型：滑动窗口内，每个words中的单词全部有且仅有出现一次
        #且长度等于串联子串的固定长度（单词定长，个数固定，所以串联子串长度也是固定的），则肯定是命中了。
        #如果words中有重复单词，那么计数时按实际个数计数即可
        #我们使用标准库函数中的collections.Counter()来计数：就是字典计数，key是单词，value是数量，自己实现也可以
        #首先，算出标准串联串的数量
        standard_joint_string_counter = collections.Counter(words)
        #将重复的单词合并了，所以这里要重置一下单词个数，用于比较单词个数
        no_of_words = len(standard_joint_string_counter)
        #其次，定义一个Counter变量用于存储滑动窗口内
        slide_window_joint_string_counter = collections.Counter()
        #再次，定义个int变量，记录滑动窗口内单词命中个数
        word_match_couter = 0
        
        #调通代码测试用
        print('standard_joint_string_counter = ', standard_joint_string_counter)
        
        #开始遍历原始字符串，当超出字符串长度时，结束遍历
        while slide_window_right_index <= raw_string_length:
            #判断是否匹配单词,
            word_match_couter = 0
            slide_window_joint_string_counter.clear()
            for start_index in range(slide_window_left_index, slide_window_right_index, single_word_length): 
                #字符串切片 取出最后一步滑动的字符串，用于匹配算法
                step_string = raw_string[start_index:(start_index + single_word_length)]                
                #如果命中单词，则存储命中记录；否则无需记录
                if standard_joint_string_counter[step_string]:
                    #滑动窗口中
                    slide_window_joint_string_counter[step_string] += 1
                    
                    #如果命中一个单词，就记录单词命中次数
                    #特殊情况：如果words中有重复单词，则命中重复次数时才一并记录
                    if slide_window_joint_string_counter[step_string] == standard_joint_string_counter[step_string]:
                        word_match_couter += 1
                
            
            #长度符合要求,如果命中了所有单词，那么就是命中了串联子串，记录结果
            if no_of_words == word_match_couter:
                result_index_list.append(slide_window_left_index)
                            
            #如果没有命中，那么滑动窗口右移
            slide_window_left_index = slide_window_left_index + 1
            slide_window_right_index = slide_window_right_index + 1
        
        #遍历完成后，返回最终处理结果
        return result_index_list   
  

if __name__ == "__main__":
    
    find_sub_string_object = Solution()
    
    #示例 1
    #输入
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    # 输出：[0,9]
    # 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
    # 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
    # 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
    # 输出顺序无关紧要。返回 [9,0] 也是可以的。
    print('示例1：', find_sub_string_object.findSubstring(s,words))

    #示例 2
    #输入
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    # 输出：[]
    # 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
    # s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
    # 所以我们返回一个空数组。
    print('示例2：', find_sub_string_object.findSubstring(s,words))

    #示例 3
    #输入：
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    # 输出：[6,9,12]
    # 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
    # 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
    # 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
    # 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
    print('示例3：', find_sub_string_object.findSubstring(s,words))
    
    #示例 4
    #输入：
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    # 输出：[8]
    # 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
    # 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
    # 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
    # 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
    print('示例4：', find_sub_string_object.findSubstring(s,words))
    
    #示例 5
    #输入
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo","barr","wing","ding","wing"]
    # 输出：[13]
    # 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
    # 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
    # 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
    # 输出顺序无关紧要。返回 [9,0] 也是可以的。
    print('示例5：', find_sub_string_object.findSubstring(s,words))
