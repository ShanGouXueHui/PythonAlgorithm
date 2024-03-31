#-*- coding:utf-8 -*-

# 需求：导航装置数量计算
# 在秋日市集景区共有N个景点，景点编号为1~N。景点内设有N−1 条双向道路，使所有景点形成了一个二叉树结构，根结点记为 root，景点编号即为节点值。
# 由于秋日市集景区的结构特殊，游客很容易迷路，主办方决定在景区的若干个景点设置导航装置，按照所在景点编号升序排列后定义装置编号为 1 ~ M。
# 导航装置向游客发送数据，数据内容为列表 [游客与装置 1 的相对距离,游客与装置 2 的相对距离,...,游客与装置 M 的相对距离]。
# 由于游客根据导航装置发送的信息来确认位置，因此主办方需保证游客在每个景点接收的数据信息皆不相同。请返回主办方最少需要设置多少个导航装置。
# 示例：
# 输入：tree_list = [1,2,null,3,4]
# 输出：2
# 解释：在景点 1、3 或景点 1、4 或景点 3、4 设置导航装置。

from collections import deque

#节点
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
   
#二叉树，用于使用List生成二叉树
class GenerateBinaryTreeByList(object):    
    def __init__(self, tree_list:list[int]):
        #定义树根
        self.tree_root = None|TreeNode
        self.generateTreeByList(tree_list)
    
    #输入的list参数，是按照层级从左到右存储
    #这种情况下使用先进先出的队列来保证节点互联顺序即可
    def generateTreeByList(self, tree_list:list[int]):
        #根节点先放入queue
        self.tree_root = TreeNode(tree_list[0])
        father_queue = deque([self.tree_root])
        #算出节点数量，用于后续计算
        tree_list_length = len(tree_list)
        #处理节点从第2个元素开始
        i = 1
        while i < tree_list_length:
            #父节点取出
            node = father_queue.popleft()
            #先处理左子节点
            node.left = TreeNode(tree_list[i]) if tree_list[i] else None
            #如果节点不为空，则放入队列，用于其子节点的计算
            if node.left:
                father_queue.append(node.left)
                
            #右节点处理
            i = i + 1
            if i >= tree_list_length:
                break
            node.right = TreeNode(tree_list[i]) if tree_list[i] else None
            if node.right:
                father_queue.append(node.left)
                
            #下一个节点处理
            i = i + 1

#标志常数
HAVE_LOCATOR = 1
NO_LOCATOR = 0
class NavigationCounter(object):
    def __init__(self, tree_root:TreeNode):
        #用于存储最少防止的导航装置数量
        self.num_of_locator = 0
        #如果是空树，则无需导航装置
        if len(tree_list) == 0:
            return
        
        #通过遍历查询导航装置的数量
        left_locator_flag = self.calculateLocators(tree_root.left)
        right_locator_flag = self.calculateLocators(tree_root.right)
        
        #针对root特殊处理
        #只有根节点，没有子树或节点是一条线，整体则仅需放置1个导航装置
        if left_locator_flag == NO_LOCATOR and right_locator_flag == NO_LOCATOR:
            self.num_of_locator = 1
        
        #针对具备双叶子节点的情况，如果单边有三叉节点，单边是一条线或None，则需增加一个导航装置
        if tree_root.right or tree_root.left:            
            #如果单边有三叉节点，单边是一条线，则需增加一个导航装置
            if (left_locator_flag == NO_LOCATOR and right_locator_flag == HAVE_LOCATOR) \
                or (left_locator_flag == HAVE_LOCATOR and right_locator_flag == NO_LOCATOR):
                self.num_of_locator += 1
        
        
    def calculateLocators(self, sub_tree:TreeNode):
        #如果子树不存在，则无需考虑导航装置，直接返回0
        if not sub_tree:
            return NO_LOCATOR
        
        left_locator_flag = self.calculateLocators(sub_tree.left)
        right_locato_flag = self.calculateLocators(sub_tree.right)
        
        #如果有左右子树（子树非Root节点处理情况），则肯定是三叉节点
        if sub_tree.left  and sub_tree.right:
            #左右均没有放导航装置,则增加一个导航装置
            if left_locator_flag == NO_LOCATOR and right_locato_flag == NO_LOCATOR:
                #增加一个导航装置
                self.num_of_locator += 1
                #返回处理结果，已有定位器，用于父节点判断是否放置导航装置
                return HAVE_LOCATOR
            #至少有一个节点已经防止了定位器
            else:
                return HAVE_LOCATOR
        #仅有左侧节点，反馈子节点的情况(节点是一条线的情况)
        if sub_tree.left:
            return left_locator_flag
        #仅有右节点，反馈子节点的情况(节点是一条线的情况)
        if sub_tree.right:
            return right_locato_flag
        #没有叶子节点，说明当前节点就是叶子节点，则无需考虑导航装置
        else:
            return NO_LOCATOR

if __name__ == '__main__':
    #实例1
    #输入：
    tree_list = [1,2,None,3,4]
    #输出：2
    bTree = GenerateBinaryTreeByList(tree_list)
    print(NavigationCounter(bTree.tree_root).num_of_locator)
    
    
    #实例2
    #输入：
    tree_list = [1,2,3,4]
    #输出：1
    bTree = GenerateBinaryTreeByList(tree_list)
    print(NavigationCounter(bTree.tree_root).num_of_locator)