#-*- coding:utf-8 -*-

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        
        #Author: ShanGouXuehui
        #Date: 2024-8-4
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile
        """
        #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组, 然后返回由这些元组组成的列表
        #如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
        # 举例：a = [1,2,3], b = [4,5,6]
        # zipped = zip(a,b) , 结果为：[(1, 4), (2, 5), (3, 6)]
        # Alice如果想要得分更多，首先要选价值最大的石子，这样可以按照同一石子综合价值，Alice得分+Bob得分排序，优先取走总分最高的
        # 数学上推导，对于排名第一的石子和第二的石子，应该取走那个呢
        # 那个分差更高，Alice选择的话，就会得分越优优势，所以对于结果（a[1] - b[2]） - （a[2] - b[1] ），
        # 如果大于0在选择a[1]，否则选择a[2]。
        # 等式做一下变换，（a[1] - b[2]） - （a[2] - b[1] ） = （a[1] + b[1]）- （a[2] + b[2]），
        # 我们就可以理解为大于零，是选择a[1] + b[1] 大的值；如果小于零，则a[2] + b[2]大的值。
        # 如果把石子编号换为i, 其实就是选择a[i] + b[i]大的值
        # 所以我们利用zip，求和，然后排序
        max_value_sorting = [[x + y, x, y] for x, y in zip(aliceValues, bobValues)]
        #sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
        #list.sort(cmp=None, key=None, reverse=False)，默认按照第1个字段排序
        max_value_sorting.sort(reverse=True)
        
        #将轮流取值结果求和
        #list[i:j:2] 一样取i到j但加入了步长 这里步长为2；也就是取每次索引位置开始+2的值
        #list[::2] 就是取奇数位,这里的i j 我们省略的话就是默认数组最开头到结尾
        accumulative_value_alice =  sum(x[1] for x in max_value_sorting[::2])
        #list[1::2] 这里缺省了j但是i定义了1 也就是从数组第二个数开始取 ，所以这个是取偶数位
        accumulative_value_bob = sum(y[2] for y in max_value_sorting[1::2])
        
        if accumulative_value_alice > accumulative_value_bob:
            return 1
        elif accumulative_value_alice < accumulative_value_bob:
            return -1
        else:
            return 0      
         
       

if __name__ == "__main__":
    cs = Solution()
    
    # 示例 1：
    # 输入：
    aliceValues = [1,3]
    bobValues = [2,1]
    # 输出：1
    # 如果 Alice 拿石子 1 （下标从 0开始），那么 Alice 可以得到 3 分。
    # Bob 只能选择石子 0 ，得到 2 分。
    # Alice 获胜。
    print('示例1：', cs.stoneGameVI(aliceValues, bobValues))
    
    # 示例 2：
    # 输入：
    aliceValues = [1,2]
    bobValues = [3,1]
    # 输出：0
    print('示例2：', cs.stoneGameVI(aliceValues, bobValues))
    
    # 示例 3：
    # 输入：
    aliceValues = [2,4,3]
    bobValues = [1,6,7]
    # 输出：-1
    print('示例3：', cs.stoneGameVI(aliceValues, bobValues))
    
    