# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:42:01 2021

@author: srinivasanl
"""
import time
saving=250
#currentValue=[1,2,3,4,5]
#futureValue=[101,102,103,104,105]
currentValue=[175,133,109,210,97]
futureValue=[200,125,128,228,133]
def argsort(array):
    return [i[0] for i in sorted(enumerate(array), key=lambda k: k[1], reverse=True)]

def selectStock(saving, currentValue, futureValue):
    # Write your code here
    
    num=len(currentValue)
    profit_arr=[0]*num
    for i in range(0,num):
        profit_arr[i]=futureValue[i]-currentValue[i]
    
    print("Profit array : ",profit_arr)
    index_max=argsort(profit_arr)
    print("Profit array index: ",index_max)
    total_future_value=0
    money_left=saving
    investment=0
    total_investment=0
    check=True
    count=0
    while(check):
        if(count>=num):
                count=0
        print("current iterator: ",count)
        inv_no=index_max[count]
        print("current inv_no: ",inv_no)
        print("current investment: ",currentValue[inv_no])
        if(currentValue[inv_no]<=money_left):
            investment=currentValue[inv_no]
            money_left=money_left-investment
            total_future_value=total_future_value+futureValue[inv_no]
            total_investment=total_investment+investment
            print("total_investment: ",total_investment)
            #print("new i", i)
            #print("num:",num)
            
                        
                    
        elif((currentValue[inv_no]>money_left) & (count==num-1)):
            check=False
        count=count+1
        time.sleep(3)
        
    max_profit=total_future_value-total_investment
    #if(max_profit<0):
    #    max_profit=0
        
    
        
    return max_profit


maximum_prof=selectStock(saving, currentValue, futureValue)
print("My max profit is: ",maximum_prof)
#index_min=min(range(len(prof)),key=prof.__getitem__)
#index_max=max(range(len(prof)),key=prof.__getitem__)
#sorted=argsort(prof)