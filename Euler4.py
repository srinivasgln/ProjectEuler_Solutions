#lst=[]
import time
t1=time.time()
maxPalin=0
count=0
for i in range(100000,999999):
    j=str(i)
    if (j==j[::-1]):
        count+=1
        for m in range(100,1000):
            if i%m==0:
                r=i/m
                if r in range(100,1000):
                    #lst.append(i)
                    if int(j)>maxPalin:
                        maxPalin=int(j)

t2=time.time()
print('the number of palidromes from range 100000 to 999999 are',count)
print('\n The time taken is', t2-t1)
print('the largest palindrome that is a multiple of 2 three digits numbers is',maxPalin)
#print('The palidromes that multiple of 2 three digits numbers is',lst)
