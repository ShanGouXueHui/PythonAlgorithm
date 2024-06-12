#-*- coding:utf-8 -*-

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-12
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type sequence: str
        :type word: str
        :rtype: int
        """
        #获取字符串和单词长度，用于后续代码复用
        sequence_length = len(sequence)
        word_length = len(word)
        
        #如果单词长度大于字符串长度，则肯定无重复单词，直接返回0
        if word_length > sequence_length:
            return 0
        
        #定义dp数组，用于存储重复值结果
        #字符下标记为i，第i个字符的连续最大重复值，记为f(i)。i便是“状态”。
        #归纳奠基（动态规划是自底向上递推，所以起始基础值必须具备）
        #在索引小于len（word）-2的位置时，将不匹配word： f(i) = 0; 初始化为0
        word_duplicate_times = [0]*sequence_length
        
        #第一个单词匹配单独处理
        if sequence[0:word_length] == word:
            word_duplicate_times[word_length-1] = 1
        
        #归纳递推（状态转移方程）
        #第i天时：max_sale = max{f(i)} i∈0~n；f(i) = f（i- len（word）） + 1 或者 f(i) = 0
        for i in range(1, sequence_length - word_length + 1):
            #下移1个字符做匹配
            #如果匹配，则f(i) = f（i- len（word）） + 1
            if word == sequence[i:i + word_length]:
                word_duplicate_times[i + word_length - 1] = word_duplicate_times[i - 1] + 1
            #如果不匹配，那么f(i) = 0
            else:
                word_duplicate_times[i + word_length - 1] = 0
        
        #返回最大连续值       
        return max(word_duplicate_times)
            



if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1
    # 输入：
    sequence = "ababc"
    word = "ab"
    # 输出：2
    # 解释："abab" 是 "ababc" 的子字符串。
    print('示例1：', cs.maxRepeating(sequence,word))
    
    # 示例 2
    #输入：
    sequence = "ababc"
    word = "ba"
    # 输出：1
    # 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
    print('示例2：', cs.maxRepeating(sequence,word))
    
    
    # 示例 3
    #输入：
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    # 输出：5
    # 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
    print('示例3：', cs.maxRepeating(sequence,word))
    
    # 示例 4
    #输入：
    sequence = "baba"
    word = "b"
    # 输出：1
    # 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
    print('示例4：', cs.maxRepeating(sequence,word))