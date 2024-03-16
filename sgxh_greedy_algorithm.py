#-*- coding:utf-8 -*-

# 需求：文本左右对齐
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，
# 且左右两端对齐的文本。尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，
# 使得每行恰好有 maxWidth 个字符。要求尽可能均匀分配单词间的空格数量。
# 如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
# 注:
# 单词是指由非空格字符组成的字符序列。每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。


#思路：先将单词分组，再处理空格问题
def greedy_text_right_alignment(words:list, maxWidth:int):
    
    #当前行的长度和内容存储
    line_width = 0
    line_string = ''

    #存储分组后的字符串
    target_string_list = []  
    final_string_list = []
    
    #将字符串分组
    num_of_words = len(words)
    tmp_index = 0
    for w in words:
        w_len = len(w)        
        #贪婪算法，如果未达到目标长度，则继续加入word       
        if w_len + line_width <= maxWidth:
            line_string = line_string + w + ' '
            line_width = len(line_string)
        #如果已经大于最大行长，则换行
        else:
            #老的一行加入目标list
            target_string_list.append(line_string.strip())
            
            #起一个新行，将word加入行首
            line_string = w + ' '                  
            line_width = len(line_string)
        
        if (tmp_index == num_of_words - 1) and (line_string != ''):
            target_string_list.append(line_string.strip())
            
        tmp_index = tmp_index + 1
            
            
    # print(target_string_list)
    
    #处理空格问题
    tmp_line = ''
    handle_lines_num = 0
    total_num_of_lines = len(target_string_list)
    for line in target_string_list:             
        #文本的最后一行应为左对齐，且单词之间不插入额外的空格。
        if handle_lines_num + 1 == total_num_of_lines:
            final_string_list.append(line.strip())
            break
        
          
        #如果当前行长正好是最长长度，则直接加入目标值
        line_len = len(line)
        if line_len == maxWidth:
            final_string_list.append(line)
            handle_lines_num = handle_lines_num + 1
            continue       
    
                
        #当将行长小于目标值，首先拆分成单词，然后填充空格
        gap_space = maxWidth - line_len
        word_list = line.split(' ')        
        world_num = len(word_list)
        
        #如果仅有一个单词，则在单词后面补充空格
        if world_num == 1:            
            tmp_gap = maxWidth - len(line)
            final_string_list.append(line + " " * tmp_gap)
            handle_lines_num = handle_lines_num + 1
            tmp_line = ''
            continue
        
        #算出来空格除以文字数-1（文字间隔数），用于均匀填补空格
        times_of_space = gap_space//(world_num - 1)
        #对于少于文字数-1（文字间隔数），则一次加上1个空格
        rest_Of_space = gap_space%world_num
        
        handled_words_no = 0
        for w in word_list:
            if handled_words_no != 0:
                #如果增加多个空格，则直接加上            
                if times_of_space != 0:
                    tmp_line = tmp_line + " " * (times_of_space + 1)
                
                #如果不足以增加多个空格，则前面是2个空格，后面word之间是保持1个空格
                if rest_Of_space > 0:
                    tmp_line = tmp_line + " " * 2                
                    rest_Of_space = rest_Of_space - 1
                else:
                    tmp_line = tmp_line + " "
                            
            tmp_line = tmp_line + w    
            handled_words_no = handled_words_no + 1
        
        final_string_list.append(tmp_line)
        handle_lines_num = handle_lines_num + 1
        tmp_line = ''
    
    print(final_string_list)
            
        
    


if __name__ == '__main__':
    #实例1
    words = ["That", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    
    #结果
    # [
    # "This    is    an",
    # "example  of text",
    # "justification."
    # ]
    greedy_text_right_alignment(words, maxWidth)
    
    #实例2
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    # 结果
    # [
    # "What   must   be",
    # "acknowledgment  ",
    # "shall be"
    # ]
    greedy_text_right_alignment(words, maxWidth)
    
    #实例3
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art",\
        "is","everything","else","we","do"]
    maxWidth = 20
    # 结果
    # [
    # "Science  is  what we",
    # "understand      well",
    # "enough to explain to",
    # "a  computer.  Art is",
    # "everything  else  we",
    # "do"
    # ]
    greedy_text_right_alignment(words, maxWidth)




