#Method one
import time
mul3=list()
mul5=list()
mul15=list()
a=int(input('\n Enter the Lower limit:\t'))
b=int(input('\n Enter the Upper limit:\t'))

t1=time.time()
for i in range(a,b):
    if i%3==0:
        mul3.append(i)
        #print('the multiples of 3 are',i)
    if i%5==0:
        mul5.append(i)
        #print('the multiples of 5 are',i)
    if i%15==0:
        mul15.append(i)

sum3=sum(mul3)
sum5=sum(mul5)
sum15=sum(mul15)
total =sum3+sum5-sum15
t2=time.time()
print('sum of multiples of 3 is ',sum3,'\nsum of multiples of 5 is',sum5,
     '\nMethod 1: the total sum of multiples of 3 and 5  is\t', total,'\nTime taken',t2-t1)
t3=time.time()
#Method two:
sm=0
for i in range(a,b):
    if (i%3==0) or (i%5==0):
        sm=sm+i
t4=time.time()
print('\nMethod 2:the total sum of multiples of 3 and 5 :',sm,'\nTime taken',t4-t3)
