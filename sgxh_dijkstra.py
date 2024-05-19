#-*- coding:utf-8 -*-

#Author: ShanGouXuehui

# 需求描述：网络延迟时间
# 输入：
# 1) 有n个网络节点，标记为1到n。
# 2) 一个列表time_cost，表示信号经过有向边的传递时间。time_cost[i] = (source_nodei, destination_nodei, costi)，其中source_nodei是源节点，destination_nodei是目标节点，costi是一个信号从源节点传递到目标节点的时间。
# 3) 从某个节点start_node发出一个信号
# 求解：
# 需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

import math
def dijkstra_get_min_latency(time_cost:list[list[int]], no_of_nodes:int, start_node:int):
    
    #定义数组用于记录最优距离，如果非直连的节点，则默认无穷大距离
    #由于数组下标从0开始，节点编号减小了1，从而使节点编号位于 [0,n−1]范围。
    distance = [math.inf] * no_of_nodes
    #源节点到源节点的距离就是0
    distance[start_node - 1] = 0
    print('distance: ', distance)
    
    #定义数组存储节点是否已获得最短距离的标志（区分已确定最短U和未确定最短距离S集群）
    confirmed_distanced_flag = [False] * no_of_nodes
    
    #Dijkstra算法求解，关键模型：若从源点start_node到当前c顶点的距离(经过最后确定顶点k)比原来距离(不经过最后确定顶点)短，则修改当前顶点的距离值，即distance[c] = min(distance[c], min(start -> k) + time_cost[k][c])
    for _ in range(no_of_nodes):
        #首先，获取下一个最短距离节点的索引，初始化为-1，标识未确定是那个节点
        confirming_node_index = -1
        # print('enumerate(confirmed_distanced_flag): ', list(enumerate(confirmed_distanced_flag)))
        #将标志通过enumerate方法将索引加上，此索引就是对应的节点索引
        for destination_node_index, flag in enumerate(confirmed_distanced_flag):
            #Python中运算符的优先级： 优先级是 not > and > or
            #将所有未确定最短距离的节点拿出，逐一比较选出离起点最短句的阶段，作为选中的最短距离节点
            if (not flag) and (confirmed_distanced_flag == -1 or distance[destination_node_index] < distance[confirming_node_index]):                
                confirming_node_index = destination_node_index
        
        #将选中节点标记为已确定最短距离
        confirmed_distanced_flag[confirming_node_index] = True
        
        #其次，将选中的新的最短距离节点作为跳板节点，刷新未确定节点中的最小距离
        #即distance[c] = min(distance[c], min(start -> k) + time_cost[k][c])
        #将标志通过enumerate方法将索引加上，此索引就是对应的节点索引
        for start_node, destination_node_index, cost in time_cost:
            if confirming_node_index == (start_node - 1):
                distance[destination_node_index-1] = min(distance[destination_node_index-1], distance[confirming_node_index] + cost)
        
        print('distance: ', distance, 'confirming_node_index = ', confirming_node_index)
    
    max_cost = max(distance)    
    # print('max_cost: ', max_cost)
    
    #由于传递信号是同时传递的，所以最大一个节点的时延就是正确的解。
    if max_cost < math.inf:
        return max_cost
    #如果不能使所有节点收到信号，返回 -1
    else:
        return -1


if __name__ == '__main__':
    #示例 1
    #输入
    time_cost = [[2,1,1],[2,3,1],[3,4,1]]
    no_of_nodes = 4
    start_node = 2
    
    #输出 2
    print(dijkstra_get_min_latency(time_cost, no_of_nodes, start_node))
    
    #示例 2
    #输入
    time_cost = [[1,2,1]]
    no_of_nodes = 2
    start_node = 1
    
    #输出 1
    print(dijkstra_get_min_latency(time_cost, no_of_nodes, start_node))
    
    
    #示例 3
    #输入
    time_cost = [[1,2,1]]
    no_of_nodes = 2
    start_node = 2
    
    #输出 -1
    print(dijkstra_get_min_latency(time_cost, no_of_nodes, start_node))