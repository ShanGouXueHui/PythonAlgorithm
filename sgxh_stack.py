#-*- coding:utf-8 -*-

# 需求：给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例:
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的柱子的高度，在这种情况下，可以接 6 个单位的雨水。 


def store_rainwater_by_stack(heights:list[int]):
    heights_length = len(heights)
    
    #形成“桶”型才能装雨水，所以至少要三个柱子；否则直接返回0
    if heights_length < 3:
        return 0
    #定义stack用于记录装雨水柱子的索引，通过索引来计算雨水的量
    index_stack = []
    #定义雨水总量变量
    total_rainwater = 0
    
    #轮询柱子，用于计算雨水
    for i in range(heights_length):
        #如果栈为空，则没有形成“桶”，无需计算装的雨水；
        #如果新的柱子大于栈顶柱子，则具备了形成了桶状的条件，立刻计算理解的雨水
        #此时栈内形状是斜向下样子，直到有了高于最低柱子的情况出来，才需要计算雨水
        while len(index_stack) and heights[i] >= heights[index_stack[-1]]:
            #栈顶保存为高低最低的柱子作为桶底
            bottom_pillar_index = index_stack.pop()        
            
            #将平齐的柱子弹出，留不住雨水，无需额外处理
            while len(index_stack) !=0 and heights[index_stack[-1]] == heights[bottom_pillar_index]:
                index_stack.pop()
                
            #如果已到了左侧边缘，则不再具备装水的条件，立刻退出
            #相当于左侧是斜向上的形状，左侧低柱子弹出，换上当前的高柱子
            if len(index_stack) == 0:
                break
                
            #桶型凹槽计算雨水
            #按照行来计算承担的雨水，所以必须算出两个柱子的间隔，掐头去尾
            no_of_pillar_gap = i - index_stack[-1] - 1
            #计算雨水总量,长度(no_of_pillar_gap)乘以高度(边缘低的柱子减去底部柱子)
            total_rainwater = total_rainwater + \
                no_of_pillar_gap * (min(heights[i], heights[index_stack[-1]]) - heights[bottom_pillar_index])
        
        index_stack.append(i)
    return total_rainwater

if __name__ == '__main__':
    #实例1
    #输入
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    #输出：6    
    print(store_rainwater_by_stack(heights))
    #输入：
    heights = [4,2,0,3,2,5]
    #输出：9
    print(store_rainwater_by_stack(heights))