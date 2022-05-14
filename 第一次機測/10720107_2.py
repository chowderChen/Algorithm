# coding: utf-8

# 學號: 10720111 / 10720107
# 姓名: 陳少暉 / 陳丕中

import sys
from math import sqrt
from functools import reduce

class Solution(object):
    numList=[]
    opList=[]
    
    def __init__(self):
        pass
    def evaluate(self):
        result = self.numList[0]
        for i in range(1, len(self.numList)):
            left = result
            right = self.numList[i]
            operator = self.opList[i - 1]
            result = operator.evaluate(left, right)
        return result

    def __repr__(self):
        result = str(self.numList[0])
        for i in range(1, len(self.numList)):
            op = self.opList[i - 1].op
            num = self.numList[i]
            result += " " + op + " " + str(num)
        return result
    
class Op(object):
    def __init__(self, op):
        self.op = op
    def evaluate(self, left, right):
        if self.op == '*':
            return left * right
        elif self.op == '+':
            return left + right
        elif self.op == '-':
            return left - right
        elif self.op == '/':
            return float(left) / right
        else:
            return "Error"

    def __repr__(self):
        return str(self.op)
        
        
def Detach(c, n):
    cardsCopy = c[:]
    cardsCopy.remove(n)
    return cardsCopy
        
def FactorOf(n):
    #回傳那個值的所有因數
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))

def is_correct(solution, value=24):
    return solution.evaluate() == value

def sort_evens_first(lst):
    """
    Sorts a list, putting the even numbers first (in ascending order)
    :param lst: The list we want to sort
    :return: The sorted list
    """
    lst.sort()
    evens = []
    odds = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds

MUL = Op('*')
PLUS = Op('+')
MINUS = Op('-')
DIV = Op('/')
OPS = [MUL, ADD, SUB, DIV]

def solve(cards,num):
    sol = Solution()
    #print(type(cards))
    
    if len(cards)<1:
        return False
    
    #case1: 只剩一個
    if len(cards)==1 :
        if cards[0]==num:
            sol.numList = num 
            sol.opList = []
            return sol
        else:
            return False
        
    #case2: 剩兩個
    if len(cards)==2 :
        #試試相乘
        if( cards[0]*cards[1]==num ):
            sol.numList = cards
            sol.opList = [MUL]
            return sol
        #試試相加
        if( cards[0]+cards[1]==num ):
            sol.numList = cards
            sol.opList = [PLUS]
            return sol
        #相減
        if cards[0]>cards[1]:
            small=cards[1]
            big=cards[0]
        else:
            small=cards[0]
            big=cards[1]
        if num>=0 :
            if big-small == num:
                sol.numList = [big, small]
                sol.opList = [MINUS]
                return sol
        else:
            if small-big == num:
                sol.numList = [small, big]
                sol.opList = [MINUS]
                return sol
        #相除
        if float(big) / small == num:
            sol.numList = [big, small]
            sol.opList = [DIV]
            return sol
            
        
        return False #若上面的都失敗了
    
    #case3: 試著把所有數字都相加
    if sum(cards) == num :
        sol.numList = cards
        for i in range(len(cards)-1):
            sol.opList.append(PLUS)
        return sol
    
    #case4: 試著把數字都相乘
    product = 1
    for i in range(len(cards)):
        product = product*cards[i]
    if product == num:
        sol.numList = cards
        for i in range(len(cards)-1):
            sol.opList.append(MUL)
        return sol
    
    #case5: 找到因數，看看剩下的能否湊成另一因數，這樣相乘就是答案
    if num > 0:
        inputList = FactorOf(num)
        factorList = []
        for i in cards:
          if i in inputList and i not in factorList:
            factorList.append(i)
        #每個factor跑一遍
        factorList.sort()
        #print(factorList)
        for factor in factorList :
            otherFactor = num / factor
            otherCards = Detach(cards, factor)
            sol = solve(otherCards, otherFactor)
            if sol:
                sol.numList.append(factor)
                sol.opList.append(MUL)
                return sol


    cardEvenFirst = sort_evens_first(cards)
    #case6: 把其中一張card跟我們要的num相減看看剩下的湊不湊得出來
    for n in cardEvenFirst:
        result = num - n
        otherCards = Detach(cards, n)
        #print('otherCards', type(otherCards))
        sol = solve(otherCards, result)
        if sol:
            sol.numList.append(n)
            sol.opList.append(PLUS)
            return sol
    #case7: 把其中一張card跟我們要的num相加看看
    for n in cardEvenFirst:
        result = num + n
        otherCards = Detach(cards, n)
        sol = solve(otherCards, result)
        if sol:
            sol.numList.append(n)
            sol.opList.append(MINUS)
            return sol
            
    #case8: 把其中一張card跟我們要的num相加看看
    cards.sort()
    for n in cards:
        result = num * n
        otherCards = Detach(cards, n)
        sol = solve(otherCards, result)
        if sol:
            sol.numList.append(n)
            sol.opList.append(DIV)
            return sol
        
    #沒答案了
    return False

cards = []
cardsInput = input("Please enter your card!")
cardsInput = cardsInput.split()
for i in range(0, len(cardsInput)):
    cards.append(int(cardsInput[i]))
#print(type(cards[0]))
#print(type(cards))
sol = solve(cards, 24)
if is_correct(sol, 24):
    print("%s"% sol)
else:
    print("NO Solution")
    

