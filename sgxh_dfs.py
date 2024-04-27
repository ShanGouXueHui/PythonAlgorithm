#-*- coding:utf-8 -*-

#Author: ShanGouXuehui

# 需求：飞行行程安排
# 1) 输入：一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。fromi 和 toi 由3大写英文字母组成，fromi != toi。
# 2) 规则：按要求根据航线列表你对该行程进行重新规划排序。
# 所有行程必须从 JFK 开始。
# 如果存在多种有效的行程，请按字典排序返回最小的行程组合。
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
# 假定所有机票至少存在一种合理的行程。
# 所有的机票必须都用一次且只能用一次。
# 4) 输出：机票列表，例如： ["JFK", "LGA"]

def dfs_itinerary(tickets: list[list[str]], start_airport:str):
    #获取行程数，也就是图的边数
    tickets_length = len(tickets)
    
    #如果只有一张机票，没得选，直接返回
    if tickets_length == 1:
        return tickets[0]
    
    #结果行程,出发行机场初始化在第一个机场位置
    final_itinerary = [start_airport,]
    
    #设置邻接表，存储出发定点对应的所有目标节点
    #存储例子：{'JFK': ['ADL', 'KND']}
    neighbor_dict = {}    
    for t in tickets:
        start, dest = t
        
        # print(' start, dest =',  start, dest)
        dest_list = neighbor_dict.get(start)
        if dest_list:
            dest_list.append(dest)
        else:
            neighbor_dict[start] = [dest,]
        # print('neighbor_dict[start] =',  neighbor_dict[start],'; neighbor_dict = ', neighbor_dict)
        
    print('neighbor_dict before sort = ', neighbor_dict)
    #目的地址按照字典序排序
    for start in neighbor_dict:
        neighbor_dict[start].sort()  
    
    print('neighbor_dict after sort = ', neighbor_dict)
    
    #定义已访问列表, 出发站点默认已访问
    visted_list = []   
    #由于存在递归逻辑，定义内嵌函数
    def dfs_calculation(current_airport:str):
        #飞机场个数 = 等于行程数 + 1； 加上出发机场，那么已完成了行程计算，直接返回
        if len(final_itinerary) == tickets_length + 1:
            return
        
        #当前机场可以飞到的机场列表，也就是图中节点的邻居们
        next_airports = neighbor_dict[current_airport]
        
        #对所有邻居节点（下一站机场）进行处理
        for ap in next_airports:
            #如果机票已经用过，则直接跳过
            key = current_airport + ':' + ap
            if key in visted_list:
                continue
            
            #如果没有访问过，则加入行程表（下一站机场列表已经做过字典排序了，所以直接取即可）
            final_itinerary.append(ap)
            #将机票标记为已访问，key格式 开始机场：目的机场
            key = current_airport + ':' + ap
            visted_list.append(key)
            
            #深度遍历，看当前机场可以到达的机场，并做处理
            dfs_calculation(ap)
    
    #启动内建函数，使用dfs算法安排行程
    dfs_calculation(start_airport)
    
    return final_itinerary
    

if __name__ == '__main__':
    #示例 1
    #输入
    start_airport = 'JFK'
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    #输出：["JFK","MUC","LHR","SFO","SJC"]
    print('示例 1',dfs_itinerary(tickets, start_airport))
    
    #示例 2
    #输入
    start_airport = 'JFK'
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
    print('示例 2',dfs_itinerary(tickets, start_airport))