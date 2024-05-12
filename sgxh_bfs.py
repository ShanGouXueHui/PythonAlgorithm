#-*- coding:utf-8 -*-

#Author: ShanGouXuehui

# 需求描述：玩家需要将箱子推到仓库中的目标位置
# 1) 游戏地图用大小为m x n的网格grid表示，其中每个元素可以是墙、地板或者是箱子。
# 2) 玩家按规则将箱子 'B' 移动到目标位置 'T' 即可完成游戏：
# 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
# 地板用字符 '.' 表示，意味着可以自由行走。
# 墙用字符 '#' 表示，意味着障碍物，不能通行。 
# 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
# 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
# 玩家无法越过箱子。
# 3) 输出：将箱子推到目标位置的最小推动次数，如果无法做到，返回-1

TARGET_VALUE = 'T'
BOX_VALUE = 'B'
PLAYER_VALUE = 'S'
WALL_VALUE = '#'

def push_box_by_bfs(grid: list[list[str]]) -> int:
    #获取推箱子游戏的地图的行数和列数
    row_length = len(grid)
    col_length = len(grid[0])
    
    #定义玩家坐标变量
    player_x = 0
    player_y = 0
    #定义箱子坐标变量
    box_x = 0
    box_y = 0
    #定义目标坐标变量
    target_x = 0
    target_y = 0
    
    #获取人、箱子、和目标位置的坐标
    get_all_coordinate = 0 
    for i in range(row_length):
        #如果坐标均已获得，则退出循环
        if get_all_coordinate == 3:
                break
        for j in range(col_length):
            #如果坐标均已获得，则退出循环
            if get_all_coordinate == 3:
                break
            #如果获取到目标位置，则记录坐标
            if grid[i][j] == TARGET_VALUE:
                target_x = i
                target_y = j
                #获取1个坐标，则标志位+1
                get_all_coordinate += 1
            #如果获取到箱子初始位置，则记录坐标
            elif grid[i][j] == BOX_VALUE:
                box_x = i
                box_y = j
                #获取1个坐标，则标志位+1
                get_all_coordinate += 1
            #如果获取到玩家初始位置，则记录坐标
            elif grid[i][j] == PLAYER_VALUE:
                player_x = i
                player_y = j
                #获取1个坐标，则标志位+1
                get_all_coordinate += 1
    
    #如果箱子本来就在目标位置，则直接返回0步
    if box_y == target_y and box_x == target_x:
        return 0
    
    #以箱子为中心，定义偏移位置：左上右下
    offset_x = [-1, 0, 1, 0]
    offset_y = [0, 1, 0, -1]
    
    
    #保存是否已经遍历节点, 推箱子的方向是什么
    visitied_box_flag = [[[False] * 4 for _ in range(row_length)] for _ in range(col_length)]
    
    #推第一步箱子
    available_offset = get_available_offset(grid, box_x, box_y, player_x, player_y)
    #如果玩家无法推箱子(无法到达箱子旁边，或者推动的方向均为墙)，则返回-1
    if not len(available_offset):
        return -1
    #记录箱子在当前位置，可以到达的位置、推箱子的方向
    box_bfs_queue_list = []
    for offset in available_offset:
        visitied_box_flag[box_x][box_y][offset]  = True
        box_bfs_queue_list.append([box_x, box_y, offset])
        
    #边界指针，滑动窗口方式，进行逐层遍历 
    queue_left_index = 0
    queue_right_index = len(box_bfs_queue_list)
    #由于是逐层访问，所以一旦达到了目标为止，肯定就是最少步骤到达目标；从原始点出发，层数记为0
    no_layer_reached_target = 0
    
    #当bfs搜索完成，则完成遍历，得出步长
    while queue_left_index < queue_right_index:
        #走一层，则增加一步
        no_layer_reached_target += 1
        #逐层处理
        for current_box_x, current_box_y, offset in box_bfs_queue_list[queue_left_index:queue_right_index]:  
            #根据保存的信息，反推出可达箱子和玩家的坐标
            next_box_x = current_box_x + offset_x[offset]
            next_box_y = current_box_y + offset_y[offset]
            
            next_player_x = current_box_x - offset_x[offset]
            next_player_y = current_box_y - offset_y[offset]
                  
            #如果已经达到终点，则直接返回步长   
            if grid[next_box_x][next_box_y] == TARGET_VALUE:
                    return no_layer_reached_target
            
            #看是否能够继续往下推箱子
            available_offset = get_available_offset(grid, next_box_x, next_box_y, next_player_x, next_player_y)
            #如果可以继续往下推箱子，则将可以推的位置加入到队列，保存为下一层可以推箱子的位置
            for offset in available_offset:
                #如果已经处理过该推箱子的方向和位置，则跳过，避免循环处理
                #如果未处理过该处理箱子的方向和位置，则加入下一层待处理
                if not visitied_box_flag[next_box_x][next_box_y][offset]:
                    visitied_box_flag[next_box_x][next_box_y][offset]  = True
                    box_bfs_queue_list.append([next_box_x, next_box_y, offset])   
                    
        #滑动窗口索引刷新，变为下一层待处理节点                           
        queue_left_index = queue_right_index
        queue_right_index = len(box_bfs_queue_list)
        
    #如果最终也没有走到目标节点，则直接返回不可达
    return -1
#获取可以推箱子的位置, 按照模型“Player - Box - New Box Place”来判断    
def get_available_offset(grid: list[list[str]], box_x, box_y, player_x, player_y):
    #获取推箱子游戏的地图的行数和列数
    row_length = len(grid)
    col_length = len(grid[0])
    
    #以箱子为中心，定义偏移位置：左上右下
    offset_x = [-1, 0, 1, 0]
    offset_y = [0, 1, 0, -1]
    
    #使用广度优先搜索算法，获取玩家可以到的位置
    player_could_reach_flag = [[False] * row_length for _ in range(col_length)]
    #玩家当前位置，肯定可以达到，首先设置为可达，作为图的初始节点
    player_could_reach_flag[player_x][player_y] = True
    #bfs逐层遍历搜索，使用queue机制来实现
    bfs_queue_list = [[player_x, player_y],]
    queue_left_index = 0
    queue_right_index = 1
    
    #当bfs搜索完成，则完成遍历，获取到了玩家可以到达的位置
    while queue_left_index < queue_right_index:
        #获取当前处理节点
        current_x, current_y = bfs_queue_list[queue_left_index]
        #当前节点游标下移一个位置，用于下一轮节点值的获取，以及是否将所有节点处理完成的判断
        queue_left_index += 1
        
        #判断直连邻居，是否可达，如果可达则加入可达队列，用于遍历
        #每个位置有四个方向可以移动，左上右下逐个判断是否为可达节点
        for offset in range(4):
            tmp_x = current_x + offset_x[offset]
            tmp_y = current_y + offset_y[offset]
            
            #偏移节点为非边界节点，未超过行和列的索引范围，且不是墙 ，那么玩家可以到达          
            if tmp_x >= 0 and tmp_x < row_length \
                and tmp_y >= 0 and tmp_y < col_length \
                    and grid[tmp_x][tmp_y] != WALL_VALUE \
                        and (not (tmp_x == box_x and tmp_y == box_y) ) \
                            and player_could_reach_flag[tmp_x][tmp_y] != True:
                                #可达的直连邻居，加入队列，用于遍历
                                bfs_queue_list.append([tmp_x, tmp_y])
                                player_could_reach_flag[tmp_x][tmp_y] = True
                                #游标右移，用于循环结束判断
                                queue_right_index += 1
        #定义list，存储可以推箱子的位置
        push_box_offset = []
        for offset in range(4):
            #推动箱子后的下一个箱子位置
            tmp_box_x = box_x + offset_x[offset]
            tmp_box_y = box_y + offset_y[offset] 
            #推动箱子时，玩家的位置，正好在箱子初始位置的另外一侧
            tmp_player_x = box_x - offset_x[offset]
            tmp_player_y = box_y - offset_y[offset] 
            
            #首先判断索引是否已经超出了地图位置
            #然后看一下，玩家是否可以到达玩家的位置
            #最后判断，箱子下一个位置是否是墙的位置
            #均满足条件，说明可以推动箱子到该位置，则加入可以推箱子位置列表中
            if tmp_box_x >= 0 and tmp_box_x < row_length \
                and tmp_box_y >= 0 and tmp_box_y < col_length \
                    and tmp_player_x >= 0 and tmp_player_x < row_length \
                        and tmp_player_y >= 0 and tmp_player_y < col_length \
                            and player_could_reach_flag[tmp_player_x][tmp_player_y] == True \
                                and grid[tmp_box_x][tmp_box_y] != WALL_VALUE:
                                    push_box_offset.append(offset)            
    return push_box_offset  
    

if __name__ == '__main__':
    #示例1
    #输入
    grid = [["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#",".",".","B",".","#"],
            ["#",".","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    #输出：3
    print('示例1：', push_box_by_bfs(grid))
    
    #示例2
    #输入
    grid = [["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#",".",".","B",".","#"],
            ["#","#","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    #输出：-1
    print('示例2：', push_box_by_bfs(grid))
    
    #示例3
    #输入
    grid = [["#","#","#","#","#","#"],
            ["#","T",".",".","#","#"],
            ["#",".","#","B",".","#"],
            ["#",".",".",".",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    #输出：5
    print('示例3：', push_box_by_bfs(grid))