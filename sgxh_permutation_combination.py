#-*- coding:utf-8 -*-
'''
1、排列需求
1）给定自然数集合，从1开始 [1,2,3,...,n]
2）给出算法计算全排列，并按照从小到大顺序排列。
3）给出最大自然数n，返回第m个排列, str格式

2、组合需求
1）给出水果种类List，包含n种水果
2）给出m个水果的组合，m <=n

'''
import itertools as it

class PermSGXH(object):
    
    def perm(self, maxNaturalNo:int, retPermNo:int):
        #生成自然数集合
        natureNoList = [y for y in range(1, maxNaturalNo + 1)]
        permList = list(it.permutations(natureNoList))
        # print(permList)
        return permList[retPermNo-1]
    
    def comb(self, fruitList:list, noOfSelected:int):
        return list(it.combinations(fruitList, noOfSelected))

if __name__ == '__main__':
    p = PermSGXH()
    
    #123
    print(p.perm(3,1))  
    #213  
    print(p.perm(3,3))
    #2314
    print(p.perm(4,9))
    
    #给出5种水果，选出3种水果的组合
    fruitList = ['苹果','火龙果','李子','桃子','香蕉']
    noOfSelected = 3
    
    print(p.comb(fruitList,noOfSelected))