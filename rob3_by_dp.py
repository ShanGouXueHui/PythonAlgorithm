#-*- coding:utf-8 -*-

from collections import deque

#节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   
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
        
        #获取子节点queue，他是下一轮处理的父节点queue
        child_queue = deque()
        
        #算出节点数量，用于后续计算
        tree_list_length = len(tree_list)
        
        #计算总的节点数
        total_node_counter = 0
        #子节点下表标识
        child_index = len(father_queue)
        total_node_counter = child_index
        
        #逐层构建二叉树
        while child_index < tree_list_length:
            #节点逐层处理，如果上层已经处理，这向下层递归
            if len(father_queue) < 1:
                #子层节点，变为父节点，子节点重新计算
                father_queue = child_queue
                child_queue = deque()
                #重新调整下一层节点子节点的开始位置
                total_node_counter += len(father_queue)
                child_index = total_node_counter 
                
            #父节点取出
            node = father_queue.popleft() 
            #空节点则直接跳过
            if not node:
                continue
              
            #先处理左子节点
            node.left = TreeNode(tree_list[child_index]) if tree_list[child_index] else None            
            #放入队列，用于其子节点的计算
            child_queue.append(node.left) 
                        
                
            #右节点处理
            child_index = child_index + 1
            if child_index >= tree_list_length:
                break
            node.right = TreeNode(tree_list[child_index]) if tree_list[child_index] else None
            child_queue.append(node.right)
                
            #下一个节点处理
            child_index = child_index + 1
            
class Solution(object):
    def rob(self, root):
        """
        #Author: ShanGouXuehui
        #Date: 2024-6-23
        #Git: https://github.com/ShanGouXueHui/PythonAlgorithm
        #Find More Python Algorithm Cases: https://m.toutiao.com/is/iYSgcfwq/
        #Personal Page: https://www.toutiao.com/c/user/token/MS4wLjABAAAAaW5663GHobdB_4icGBE0z2IJSWBSYeEAmoCfHTazjhTREfuBFo6wZCPR34-atRpn/?source=profile

        :type root: TreeNode
        :rtype: int
        """
        
        #如果root仅有一个元素，则返回root金额
        if  not root.left and not root.right:
            return root.val
        
        #整一个可读的名字        
        room_tree_root:TreeNode = root
        #获取左右孩子可以盗取现金的金额，返回值格式[not_selected_max_amount, selected_max_amount]
        left_child_amount = self.dfs_for_rob(room_tree_root.left)
        right_child_amount = self.dfs_for_rob(room_tree_root.right)
        
        #root被盗窃：f[i][1] = f[i->left][0] + f[i->right][0] + root[i]
        selected_room_amount = left_child_amount[0] + right_child_amount[0] + room_tree_root.val
        #root未被盗窃：f[i][0] = max(f[i->left][0],f[i->left][1]) + max(f[i->right][0],f[i->right][1])
        not_selected_room_amount = max(left_child_amount[0], left_child_amount[1]) + max(right_child_amount[0], right_child_amount[1])
        
        #最终，深度遍历这棵二叉树，比较f[root][1]和f[root][0]，大者为最大金额解。
        return max(not_selected_room_amount, selected_room_amount)
           
    #深度优先算法，返回值为[not_selected_max_amount, selected_max_amount]
    #由于并无复用场景，无需保存中间计算过程   
    def dfs_for_rob(self, tree_root: TreeNode):
        #如果是空节点，无论则直接返回金额0，格式[not_selected_max_amount, selected_max_amount]
        if not tree_root:
            return [0,0]
        
        #获取左右孩子可以盗取现金的金额，返回值格式[not_selected_max_amount, selected_max_amount]
        left_child_amount = self.dfs_for_rob(tree_root.left)
        right_child_amount = self.dfs_for_rob(tree_root.right)
        
        #状态转移返程
        #f[i][1] = f[i->left][0] + f[i->right][0] + root[i]
        #f[i][0] = max(f[i->left][0],f[i->left][1]) + max(f[i->right][0],f[i->right][1])
        #tree_root.max_amount = [not_selected_max_amount, selected_max_amount]
        selected_room_amount = left_child_amount[0] + right_child_amount[0] + tree_root.val
        not_selected_room_amount = max(left_child_amount[0], left_child_amount[1]) + max(right_child_amount[0], right_child_amount[1])
        
        #返回计算值，格式[not_selected_max_amount, selected_max_amount]
        return [not_selected_room_amount, selected_room_amount]
        

            
if __name__ == "__main__":
    cs = Solution()
    
    #示例1
    # 输入
    root = [3,2,3,None,3,None,1]
    # 输出: 7 
    # 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
    
    #绕不过计算子节点的逻辑，我们先将list转化为带指针的二叉树，简化动态规划逻辑        
    room_tree_root:TreeNode = GenerateBinaryTreeByList(root).tree_root
    print('示例1：', cs.rob(room_tree_root))
    
    #示例2
    # 输入: 
    root = [3,4,5,1,3,None,1]
    # 输出: 9
    # 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
    
    #绕不过计算子节点的逻辑，我们先将list转化为带指针的二叉树，简化动态规划逻辑
    room_tree_root:TreeNode = GenerateBinaryTreeByList(root).tree_root
    print('示例2：', cs.rob(room_tree_root))