#-*- coding:utf-8 -*-

# 需求：用一辆卡车把一些箱子从仓库运送到码头。这辆卡车每次运输有箱子数目的限制 和总重量的限制 。
# 输入：
# 一个箱子数boxes和三个整数portsCount, maxBoxes和maxWeight，其中 boxes[i] = [portsi, weighti] 。
# portsi表示第i 个箱子需要送达的码头，weightsi是第 i 个箱子的重量。portsCount 是码头的数目。maxBoxes 和 maxWeight 分别是卡车每趟运输箱子数目和重量的限制。
# 运输规则：
# 箱子需要按照数组顺序运输，同时每次运输需要遵循以下步骤：
# 1）卡车从 boxes 队列中按顺序取出若干个箱子，但不能超出maxBoxes和 maxWeight限制。
# 2）对于在卡车上的箱子，我们需要按顺序处理它们，卡车会通过一趟行程将最前面的箱子送到目的地码头并卸货。如果卡车已经在对应的码头，那么不需要额外行程，箱子也会立马被卸货。如果切换码头，则增加1趟行程
# 3）卡车上所有箱子都被卸货后，卡车需要一趟行程回到仓库，从箱子队列里再取出一些箱子。
# 4) 卡车在将所有箱子运输并卸货后，最后必须回到仓库。
# 输出(求解)：
# 请你返回将所有箱子送到相应码头的最少行程次数

from collections import deque

def box_deliver_by_min_steps(boxes:list[list[int]], portsCount:int, maxBoxes:int, maxWeight:int):
    #获取箱子个数，避免重复计算
    boxes_length = len(boxes)
    #由于码头变换，就会增加行程，由于箱子是固定顺序的，所以这个值是固定的，先计算出来累计值，用作状态转移方程的备用
    #同时由于箱子累计重量也做一下提前计算
    #首先初始化累计码头变换次数和累计重量list变量, 增加一个状态：未装箱，即0箱的状态作为初始值
    port_change_accumulate = [0] * (boxes_length + 1)
    weight_accumulate = [0] * (boxes_length + 1)
    
    #首个箱子的值特殊处理
    port_change_accumulate[1] = 0
    weight_accumulate[1] = boxes[0][1]
    #计算累计值
    for i in range(2, boxes_length + 1):
        #累计值多了一个初始值，所以boxes索引偏移1位
        #如果相邻两个码头一样，则不增加行程，否则增加1 的行程
        port_change_accumulate[i] =  port_change_accumulate[i - 1 ] + (0 if boxes[i-2][0] == boxes[i-1][0] else 1)
        weight_accumulate[i] = weight_accumulate[i-1] + boxes[i-1][1]
    
    # print(port_change_accumulate)
    # print(weight_accumulate)
    #装车箱子滑动空间内，记录累计行程最小的装箱记录
    box_in_trunk_queue = deque([0])
    #最小行程总数
    min_trips = [0] * (boxes_length + 1)
    #通过状态转移方程，按照卡车容量(Queue)遍历，求最小总计行程
    for i in range(1, boxes_length + 1):
        #如果车已经装满(箱子个数或重量)，则开始下一车装箱的遍历
        #box_in_trunk_queue[0]存储的是上一车最后一个箱子索引
        # print(box_in_trunk_queue)
        while (i - box_in_trunk_queue[0]) > maxBoxes or \
            (weight_accumulate[i] - weight_accumulate[box_in_trunk_queue[0]]) > maxWeight:
            #FIFO队列，车已满则将最先装车的箱子弹出，
            #作为上一车的最后一个箱子, 遍历后已求出的该箱子装车后的最优行程
            box_in_trunk_queue.popleft()
        #状态转移方程实现：min_trips[i] = min{min_trips[j] + port_change_times[j + 1, i] + 2}
        #状态转移方程 第1步 - 逐个箱子计算行程：min_trips[i] = min_trips[j] + port_change_times[j + 1, i] + 2
        #j就是box_in_trunk_queue[0], 上一车最后一个装车的箱子的索引(下标)
        min_trips[i] = min_trips[box_in_trunk_queue[0]] + (port_change_accumulate[i] - port_change_accumulate[box_in_trunk_queue[0] + 1]) + 2
        
        #状态转移方程 第2步 - 状态转移方程中 比较行程后 获取最小值
        #比较滑动空间内，每个箱子的总计行程数，仅保留最小行程总数的索引记录        
        while min_trips and (min_trips[i] <= min_trips[box_in_trunk_queue[-1]]):
            #LIFO队列，按装箱次序比较，并弹出有较大行程数，仅保留最小行程数的箱子(索引)，作为“这一车最后一个箱子”
            box_in_trunk_queue.pop()
        box_in_trunk_queue.append(i)
        
    #返回最优解
    return min_trips[boxes_length]

if __name__ == '__main__':
    #测试1
    boxes = [[1,1],[2,1],[1,1]]
    portsCount = 2
    maxBoxes = 3
    maxWeight = 3
    #输出：4
    print('测试1: ',box_deliver_by_min_steps(boxes, portsCount, maxBoxes, maxWeight))
    
    #测试2
    boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]]
    portsCount = 3
    maxBoxes = 3
    maxWeight = 6
    #输出：6
    print('测试2: ',box_deliver_by_min_steps(boxes, portsCount, maxBoxes, maxWeight))
    
    #测试3
    boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]]
    portsCount = 3
    maxBoxes = 6
    maxWeight = 7
    #输出：6
    print('测试3: ',box_deliver_by_min_steps(boxes, portsCount, maxBoxes, maxWeight))
    
    #测试4
    boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
    portsCount = 5
    maxBoxes = 5
    maxWeight = 7
    #输出：14
    print('测试4: ',box_deliver_by_min_steps(boxes, portsCount, maxBoxes, maxWeight))